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

# install and enable pre-commit hooks (Day 2)
pre-commit install
# run hooks against all files once:
pre-commit run --all-files

# To add changes and commit:
git add .
git commit -m "chore: linters & repo polish"

# Notes:
# - If mypy reports too many issues initially, run:
#     mypy --install-types --non-interactive
#   then re-run pre-commit hooks.
