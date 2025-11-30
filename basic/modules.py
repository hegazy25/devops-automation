# Import standard library modules
import os
import sys
from datetime import datetime

# Check current directory
print(os.getcwd())

# Get current time
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Working with files
import json

data = {"name": "app", "version": "1.0"}
with open("config.json", "w") as f:
    json.dump(data, f)

# Read file
with open("config.json", "r") as f:
    config = json.load(f)
print(config)
