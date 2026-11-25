# Windows: list the display modes and try to switch the screen to Width x Height.
# Usage: pwsh scripts/desktop/set_resolution.ps1 -List | -Width 1920 -Height 1080
# Prints the mode in force afterwards. Exit code is 0 even if the change is refused (the caller reads the output).
param([int]$Width = 0, [int]$Height = 0, [switch]$List)
Add-Type @"
using System; using System.Runtime.InteropServices;
public class Disp {
  [StructLayout(LayoutKind.Sequential, CharSet=CharSet.Ansi)]
  public struct DEVMODE {
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst=32)] public string dmDeviceName;
    public short dmSpecVersion; public short dmDriverVersion; public short dmSize; public short dmDriverExtra;
    public int dmFields; public int dmPositionX; public int dmPositionY; public int dmDisplayOrientation; public int dmDisplayFixedOutput;
    public short dmColor; public short dmDuplex; public short dmYResolution; public short dmTTOption; public short dmCollate;
    [MarshalAs(UnmanagedType.ByValTStr, SizeConst=32)] public string dmFormName;
    public short dmLogPixels; public int dmBitsPerPel; public int dmPelsWidth; public int dmPelsHeight; public int dmDisplayFlags; public int dmDisplayFrequency;
    public int dmICMMethod; public int dmICMIntent; public int dmMediaType; public int dmDitherType; public int dmReserved1; public int dmReserved2; public int dmPanningWidth; public int dmPanningHeight;
  }
  [DllImport("user32.dll", CharSet=CharSet.Ansi)] public static extern bool EnumDisplaySettings(string dev, int mode, ref DEVMODE dm);
  [DllImport("user32.dll", CharSet=CharSet.Ansi)] public static extern int ChangeDisplaySettings(ref DEVMODE dm, int flags);
}
"@
function New-Dm { $d = New-Object Disp+DEVMODE; $d.dmSize = [int16][Runtime.InteropServices.Marshal]::SizeOf($d); $d }
function Get-Current { $d = New-Dm; [void][Disp]::EnumDisplaySettings([NullString]::Value, -1, [ref]$d); $d }
$cur = Get-Current
"current: $($cur.dmPelsWidth)x$($cur.dmPelsHeight) @ $($cur.dmBitsPerPel)bpp"
if ($List -or $Width -eq 0) {
  $modes = @{}; $i = 0; $d = New-Dm
  while ([Disp]::EnumDisplaySettings([NullString]::Value, $i, [ref]$d)) { $modes["$($d.dmPelsWidth)x$($d.dmPelsHeight)"] = 1; $i++ }
  "modes ($i entries): " + (($modes.Keys | Sort-Object { [int]($_ -split 'x')[0] }) -join ' ')
  exit 0
}
# Wanted size first, then the common smaller ones that fit inside it (the hosted display accepts custom sizes up to 1920x1080 only)
$tries = @("${Width}x${Height}") + @('1920x1080','1600x900','1366x768','1280x800','1280x720','1024x768') |
  Where-Object { $w,$h = $_ -split 'x'; [int]$w -le $Width -and [int]$h -le $Height } | Select-Object -Unique
foreach ($t in $tries) {
  $w,$h = $t -split 'x'
  $d = Get-Current; $d.dmPelsWidth = [int]$w; $d.dmPelsHeight = [int]$h; $d.dmFields = 0x80000 -bor 0x100000
  $test = [Disp]::ChangeDisplaySettings([ref]$d, 2)      # CDS_TEST
  "test ${t}: code $test (0 = supported)"
  if ($test -eq 0) { "apply: code " + [Disp]::ChangeDisplaySettings([ref]$d, 0); Start-Sleep 2; break }
}
$cur = Get-Current
"now: $($cur.dmPelsWidth)x$($cur.dmPelsHeight) (wanted ${Width}x${Height})"
