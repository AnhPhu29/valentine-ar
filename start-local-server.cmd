@echo off
REM Valentine AR - Local Server Setup (Windows CMD)

setlocal enabledelayedexpansion

echo.
echo ================================
echo   Valentine AR - Local Server Setup
echo ================================
echo.

REM Check if Node.js is installed
node -v >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Node.js not found!
    echo [INFO] Install from: https://nodejs.org/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('node -v') do set NODE_VERSION=%%i
echo [OK] Node.js version: %NODE_VERSION%

REM Check http-server
echo.
echo [INFO] Checking http-server...

npm list -g http-server >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing http-server globally...
    npm install -g http-server
)

echo [OK] http-server is ready

REM Start server
echo.
echo [INFO] Starting local server...
echo.
echo.
echo ================================
echo   LOCAL SERVER READY
echo ================================
echo.

for /f "tokens=1" %%a in ('ipconfig ^| findstr "IPv4"') do (
    for /f "tokens=2 delims=:" %%b in ('ipconfig ^| findstr "IPv4"') do (
        set LOCAL_IP=%%b
        set LOCAL_IP=!LOCAL_IP: =!
    )
)

echo [TIP] Open this URL on your phone:
echo.
echo   http://YOUR_PC_IP:8080/valentine-ar.html
echo.
echo [TIP] To find your PC IP, run in another command prompt:
echo   ipconfig
echo.
echo [TIP] Look for line starting with "IPv4 Address"
echo.
echo [WARNING] Press Ctrl+C to stop server
echo.
echo ================================
echo.

http-server -c-1 -p 8080

pause
