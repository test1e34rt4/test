# vuln.py
import os
import subprocess

def run_command(user_input):
    # Intentional CodeQL-detectable command injection vulnerability
    os.system("echo " + user_input)

def another_insecure_func(user_input):
    subprocess.call("ls " + user_input, shell=True)
