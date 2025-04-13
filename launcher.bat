@echo off
title XTCPP Launcher
cd /d %~dp0

echo Launching XTCPP Agents...
timeout /t 1 >nul

start "XTCPP_0" cmd /k "python agents\xtcpp_0.py"
timeout /t 1 >nul

start "XTCPP_1" cmd /k "python agents\xtcpp_1.py"
timeout /t 1 >nul

start "XTCPP_2" cmd /k "python agents\xtcpp_2.py"
timeout /t 1 >nul

start "XTCPP_3" cmd /k "python agents\xtcpp_3.py"

echo All agents launched. Windows should now appear.
exit
