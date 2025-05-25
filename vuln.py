# vuln.py
import os
import subprocess

def vulnerable_os_call(user_input):
    os.system("echo " + user_input)  # 🔥 CodeQL will flag this (command injection)

def vulnerable_subprocess_call(user_input):
    subprocess.call("ls " + user_input, shell=True)  # 🔥 CodeQL alert

def insecure_compare(pwd1, pwd2):
    if pwd1 == pwd2:  # 🔥 weak equality check (CodeQL flags known in some configs)
        print("Passwords match")

def hardcoded_secret():
    api_key = "sk_live_hardcoded_key"  # 🔥 Secret scanning alert
    return api_key
