"""0.1 Setup - run with:  uv run python lessons/l01_setup.py"""
import sys

print("Hello from Python", sys.version.split()[0])
print("Running inside:", sys.prefix)  # path of the .venv uv created
