@echo off
cd /d C:\Users\prana\hbb-site
python scripts\preflight.py
exit /b %ERRORLEVEL%
