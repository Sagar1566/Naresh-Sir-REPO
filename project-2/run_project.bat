@echo off
echo ========================================
echo   Student Pass/Fail ML Project
echo ========================================
echo.

echo [1/3] Checking Python installation...
python --version
if errorlevel 1 (
    echo ERROR: Python is not installed!
    echo Please install Python from https://www.python.org/
    pause
    exit
)
echo.

echo [2/3] Installing required libraries...
pip install -r requirements.txt
echo.

echo [3/3] Running ML model...
cd model
python train.py
cd ..
echo.

echo ========================================
echo   Project completed successfully!
echo   Check output/result.csv for results
echo ========================================
pause
