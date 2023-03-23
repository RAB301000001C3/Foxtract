@echo off
setlocal

set source=sqlite
set destination=C:\sqlite3

if not exist "%source%" (
  echo Source directory not found.
  exit /b 1
)

if exist "%destination%" (
  echo Destination directory already exists.
  exit /b 1
)

xcopy "%source%" "%destination%" /s /i

if not exist "%destination%" (
  echo Failed to copy directory.
  exit /b 1
)

setx /M PATH "%PATH%;C:\sqlite3"

echo C:\sqlite3 added to Path environment variable.
