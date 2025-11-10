@echo off
REM -- 1. VENV Activate --
REM Check if venv exists and activate it
if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo Error: Virtual environment 'venv' not found. Please run setup.bat first.
    goto :eof
)

REM -- 2. Run the Python Script --
REM Jo bhi arguments (.bat file ke baad) diye gaye hain, unhe my_bot.py ko pass karo
python my_bot.py %*

REM -- 3. Deactivate VENV --
REM Script khatam hone ke baad venv ko deactivate kar do
deactivate

:eof