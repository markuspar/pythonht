import os

os.environ['TCL_LIBRARY'] = "C:\\Python3\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Python3\\tcl\\tk8.6"
from cx_Freeze import setup, Executable
import sys
build_exe_options = {"packages": ["PyQt5","pyautogui","pyDes"], "excludes": ["tkinter","cv2","numpy","matplotlib","PIL", "flask","Crypto","virtualenv_support","pip",
"email","html","pymsgbox","pytweening","xml","urlib","http",]}

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(

	name = "Testi",
	version = "0.1",
	description = "HelperBot",
       	options = {"build_exe": build_exe_options},
	executables = [Executable("window.py", base=base)],
)