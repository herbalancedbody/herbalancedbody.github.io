@echo off
schtasks.exe /Create /TN "hbb-preflight" /TR "\"C:\Users\prana\hbb-site\scripts\run_preflight.cmd\"" /SC DAILY /ST 00:00 /F
