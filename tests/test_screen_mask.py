"""Pixel masking of screenshots while QA secrets are set (Bold 28.11): a SYNTHETIC secret, no real screen, no PNG written.
Cases asked for: no tree, a system input screen, a partly visible field, a secret piece in a non-field element."""
import ast, os, re, shutil, tempfile, unittest, glob
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
FAKE = "Zq7-synthetic-Pw!"   # not a real credential


def load(rel):
    src = (ROOT / rel).read_text()
    tree = ast.parse(src)
    ns = {"re": re, "os": os, "shutil": shutil, "tempfile": tempfile, "_SECRETS": [FAKE]}
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name in ("_redact", "mask", "capture_png", "dump_ui"):
            exec(compile(ast.Module([node], []), rel, "exec"), ns)
    return ns


BLACK, WHITE = (0, 0, 0), (255, 255, 255)


class IOSMask(unittest.TestCase):
    ns = load("scripts/ios/screen.py")

    def run_mask(self, els, size=(390, 844)):
        img = Image.new("RGB", size, WHITE)
        self.ns["mask"](img, els, 1.0, [FAKE])
        return img

    def test_no_tree_withholds_the_whole_screen(self):
        img = self.run_mask([])
        self.assertEqual(img.getpixel((10, 10)), BLACK)
        self.assertEqual(img.getpixel((380, 830)), BLACK)

    def test_system_secure_field_is_painted(self):   # e.g. the iOS «Save password» / sign-in sheet
        img = self.run_mask([("SecureTextField", "Password", "•••••", {"x": 20, "y": 400, "width": 350, "height": 44}),
                             ("StaticText", "Save password?", "", {"x": 20, "y": 300, "width": 350, "height": 20})])
        self.assertEqual(img.getpixel((100, 420)), BLACK)
        self.assertEqual(img.getpixel((100, 310)), WHITE)   # plain text stays readable

    def test_partly_visible_field_is_clipped_and_painted(self):
        img = self.run_mask([("TextField", "Email", "owner@x.uz", {"x": -40, "y": 820, "width": 500, "height": 60})])
        self.assertEqual(img.getpixel((5, 830)), BLACK)
        self.assertEqual(img.getpixel((385, 843)), BLACK)

    def test_secret_piece_in_a_non_field_element(self):   # the password typed into the e-mail field, shown in a label, cut
        img = self.run_mask([("StaticText", "owner@x.uz" + FAKE[:9], "", {"x": 10, "y": 100, "width": 200, "height": 20}),
                             ("Button", "Войти", "", {"x": 10, "y": 200, "width": 200, "height": 44})])
        self.assertEqual(img.getpixel((50, 110)), BLACK)
        self.assertEqual(img.getpixel((50, 220)), WHITE)


class AndroidMask(unittest.TestCase):
    ns = load("scripts/android/screen.py")

    def run_mask(self, nodes, size=(1080, 2400)):
        img = Image.new("RGB", size, WHITE)
        self.ns["mask"](img, nodes, [FAKE])
        return img

    def test_no_tree_withholds_the_whole_screen(self):
        self.assertEqual(self.run_mask([]).getpixel((500, 1200)), BLACK)

    def test_password_and_edit_fields_are_painted(self):
        img = self.run_mask([{"class": "android.widget.EditText", "password": "true", "text": "", "bounds": "[40,900][1040,1030]"},
                             {"class": "android.widget.TextView", "text": "Kirish", "bounds": "[40,1200][1040,1300]"}])
        self.assertEqual(img.getpixel((500, 950)), BLACK)
        self.assertEqual(img.getpixel((500, 1250)), WHITE)

    def test_partly_visible_field_is_clipped_and_painted(self):
        img = self.run_mask([{"class": "android.widget.EditText", "text": "", "bounds": "[0,2300][1080,2600]"}])
        self.assertEqual(img.getpixel((10, 2399)), BLACK)

    def test_secret_piece_in_a_non_field_node(self):
        img = self.run_mask([{"class": "android.view.View", "content-desc": "x" + FAKE[3:12], "bounds": "[0,100][500,200]"}])
        self.assertEqual(img.getpixel((10, 150)), BLACK)


class NoRawFiles(unittest.TestCase):
    """The entrypoints keep no raw screen or tree anywhere, also when capture or read fails."""
    ios = load("scripts/ios/screen.py")
    android = load("scripts/android/screen.py")

    def shots_left(self):
        return glob.glob(os.path.join(tempfile.gettempdir(), "intop-shot-*"))

    def test_ios_capture_is_read_into_memory_and_the_temp_dir_removed(self):
        before = set(self.shots_left())
        data = self.ios["capture_png"](lambda path: open(path, "wb").write(b"\x89PNGfake"))
        self.assertEqual(data, b"\x89PNGfake")
        self.assertEqual(set(self.shots_left()), before)

    def test_ios_capture_failure_leaves_nothing(self):
        before = set(self.shots_left())
        def boom(path):
            open(path, "wb").write(b"half")
            raise RuntimeError("simctl died")
        with self.assertRaises(RuntimeError):
            self.ios["capture_png"](boom)
        self.assertEqual(set(self.shots_left()), before)

    def test_android_tree_through_stdout_touches_no_file(self):
        calls = []
        def adb(*a):
            calls.append(a)
            return 'UI hierchary dumped to: /dev/tty <?xml version="1.0"?><hierarchy><node/></hierarchy>\n'
        xml = self.android["dump_ui"](adb)
        self.assertTrue(xml.startswith("<") and xml.endswith("</hierarchy>"))
        self.assertEqual(len(calls), 1)                      # no file written, nothing to remove

    def test_android_fallback_file_is_removed_even_when_the_read_fails(self):
        calls = []
        def adb(*a):
            calls.append(a)
            if a[:3] == ("exec-out", "uiautomator", "dump"):
                return "ERROR: could not open /dev/tty"
            if a[0] == "exec-out" and a[1] == "cat":
                raise RuntimeError("adb lost the device")
            return ""
        with self.assertRaises(RuntimeError):
            self.android["dump_ui"](adb)
        rm = [a for a in calls if a[:3] == ("shell", "rm", "-f")]
        self.assertEqual(len(rm), 1)
        self.assertTrue(rm[0][3].startswith("/data/local/tmp/ui-"))


if __name__ == "__main__":
    unittest.main()
