cd ..

REM Create a Python virtual environment
python -m venv .venv

REM Activate the virtual environment
call .venv\Scripts\activate

REM Install the required packages
pip install -r dev_setup/requirements.txt

REM Deactivate the virtual environment
deactivate