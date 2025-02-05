import ctypes
import pathlib as p
import os
import sys
import logging as log
import shutil as g
# Declare Numbers for Init MessageBoxW or MessageBoxA
MB_ABORTRETRYIGNORE = int(0x00000002)
MB_CANCELTRYCONTINUE = int(0x00000006)
MB_HELP = int(0x00004000)
MB_OK = int(0x0)
MB_OKCANCEL = int(0x1)
MB_RETRYCANCEL = int(0x00000005)
MB_YESNO = int(0x00000004)
MB_YESNOCANCEL = int(0x00000003)
MB_ICONWARNING = int(0x00000030)
MB_ICONINFORMATION = int(0x00000040)
MB_ICONQUESTION = int(0x00000020)
MB_ICONERROR = int(0x00000010)
IDABORT = int(0x3)
IDCANCEL = int(0x2)
IDCONTINUE = int(0x11)
IDIGNORE = int(0x5)
IDNO = int(0x7)
IDOK = int(0x1)
IDRETRY = int(0x4)
IDTRYAGAIN = int(0x10)
IDYES = int(0x6)
CoverCorp_Holoearth = "E:\\COVER corp\\HoloearthApps\\Holoearth" # Make Sure what this is Correct Folder!!!
def MBOX_Main():
    user32 = ctypes.WinDLL("User32.dll")
    if user32.MessageBoxA(0, bytes("Are you sure to Run This Bypass KS_Diagnostics_Process.dll for Game Holoearth?!", "utf-8"), bytes("KSDiagnosticsProcessInstaller-HoloearthEdition", "utf-8"), MB_YESNO + MB_ICONQUESTION) == IDYES:
        if p.Path(CoverCorp_Holoearth).is_dir():
            print("Founded This Dir... This Bypasss and Installer will be Executed!!!")
            if os.path.dirname(CoverCorp_Holoearth + "\\Holoearth_Data\\Plugins\\x86_64\\KS_Diagnostics_Process.dll") == "":
                print("Not Founded Or This Plugin isn't Included in this Game... Pls Make Sure what This Game is Supported by KS_Diagnostics_Process.dll!!!")
                exit(334)
            os.rename(str(CoverCorp_Holoearth + "\\Holoearth_Data\\Plugins\\x86_64\\KS_Diagnostics_Process.dll"), str(CoverCorp_Holoearth + "\\Holoearth_Data\\Plugins\\x86_64\\KS_Diagnostics_Process.renamed.dll"))
            g.copy2(str("KS_Diagnostics_Process.dll"), str(CoverCorp_Holoearth + "\\Holoearth_Data\\Plugins\\x86_64\\KS_Diagnostics_Process.dll"))
            print("Renamed!!! Made by RikkoMatsumatoOfficial!!!")
            exit(334)
        else:
            exit(322)

if __name__ == "__main__":
    MBOX_Main()