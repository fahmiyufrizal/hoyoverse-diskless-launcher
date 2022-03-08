# Hoyoverse Hybrid-Diskless Launcher
# fahmiyufrizal@2022

# Import module
from os import path
import os
import configparser
import subprocess
import pathlib
import asyncio
from configparser import ConfigParser, ExtendedInterpolation

# title
os.system(
    "title Hoyoverse Hybrid Diskless Launcher v1.0 [github.com/fahmiyufrizal]")

# check folder _fahmiyufrizal, if not exist create
pathlib.Path("_fahmiyufrizal").mkdir(parents=True, exist_ok=True)
dp0 = os.getcwd()

# fix var hoyoverse
newPath = dp0.replace(os.sep, '/')

# path
mihoyo = path.expandvars(r'%userprofile%\AppData\LocalLow\miHoYo')
honkai3 = path.expandvars(r'%userprofile%\AppData\LocalLow\miHoYo\Honkai Impact 3')
hi3_exe = (r'Games\BH3.exe')
gi_exe = (r'Genshin Impact Game\GenshinImpact.exe')

# clear mihoyo
mihoyo_cl = open(r'mihoyo_cl.bat','w+')
mihoyo_cl.write('IF EXIST %userprofile%\AppData\LocalLow\miHoYo RD /S /Q %userprofile%\AppData\LocalLow\miHoYo')
mihoyo_cl.close()
subprocess.call([r'mihoyo_cl.bat'])
os.remove('mihoyo_cl.bat')
pathlib.Path(mihoyo).mkdir(parents=True, exist_ok=True)

# main
os.system('cls')
print("  ")
print(" Hoyoverse Hybrid Diskless Launcher")
print(" fahmiyufrizal@2022")
print(" ")

# detect hoyoverse
protected