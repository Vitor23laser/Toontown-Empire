@echo off

title Gravity Falls
rem Define some constants for our AI server:
set MAX_CHANNELS=999999
set STATESERVER=4002
set ASTRON_IP=127.0.0.1:7100
set EVENTLOGGER_IP=127.0.0.1:7198

set DISTRICT_NAME=Gravity Falls
set BASE_CHANNEL=401000000

echo ===============================
echo Starting Toontown Empire AI server...
echo ppython: "dependencies/panda/python/ppython.exe"
echo District name: %DISTRICT_NAME%
echo Base channel: %BASE_CHANNEL%
echo Max channels: %MAX_CHANNELS%
echo State Server: %STATESERVER%
echo Astron IP: %ASTRON_IP%
echo Event Logger IP: %EVENTLOGGER_IP%
echo ===============================

cd ../../

:main
"dependencies/panda/python/ppython.exe" ^
	-m toontown.ai.ServiceStart ^
	--base-channel %BASE_CHANNEL% ^
	--max-channels %MAX_CHANNELS% ^
	--stateserver %STATESERVER% ^
	--astron-ip %ASTRON_IP% ^
	--eventlogger-ip %EVENTLOGGER_IP% ^
	--district-name "%DISTRICT_NAME%"
pause
goto main

