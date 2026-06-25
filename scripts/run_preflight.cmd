@echo off
if not exist C:\Users\prana\hbb-site\logs mkdir C:\Users\prana\hbb-site\logs
cd /d C:\Users\prana\hbb-site
python scripts\preflight.py > C:\Users\prana\hbb-site\logs\preflight.log 2>&1
exit /b %ERRORLEVEL%
