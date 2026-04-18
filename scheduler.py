import time
import subprocess

while True:

    subprocess.run(["python","run.py"])

    time.sleep(86400)  # run daily
