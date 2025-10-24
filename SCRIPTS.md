## Local setup commands (copy & paste)

# create project directory and enter it (if not already)
mkdir -p luxuryconnect && cd luxuryconnect

# create virtualenv (Python 3.12 required)
python3.12 -m venv .venv
source .venv/bin/activate

# install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install -r dev-requirements.txt

# initialize django project (Day 3 planned)
# django-admin startproject luxuryconnect .
