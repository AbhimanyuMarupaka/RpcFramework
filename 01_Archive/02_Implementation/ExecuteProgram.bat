@echo off
cd /d "%~dp0"

echo echo The Client App calls the add(int a, int b) method, allowing you to optionally provide values for a and b. If no values are given, the program will use the default values specified within the code.

:prompt_user
set /p user_input=Do you want to provide values for a and b? (y/n): 
if /i "%user_input%"=="y" (
    goto input_values
) else if /i "%user_input%"=="n" (
    goto run_default
) else (
    echo Invalid input. Please enter "y" for yes or "n" for no.
    goto prompt_user
)

:input_values
set /p a=Enter the first integer (a): 
set /p b=Enter the second integer (b): 
python 01_ClientRpc/main.py --a %a% --b %b%
goto end

:run_default
echo No inputs provided, using default values in the Python program.
python 01_ClientRpc/main.py
goto end

:end
pause
