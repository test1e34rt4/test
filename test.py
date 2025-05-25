import os
import subprocess
import pickle
import base64
import tempfile

# 🔥 Command injection
def dangerous_os(user_input):
    os.system("echo " + user_input)

# 🔥 Shell injection
def dangerous_subprocess(user_input):
    subprocess.call("ls " + user_input, shell=True)

# 🔥 Unsafe deserialization
def unsafe_pickle():
    data = pickle.loads(base64.b64decode("gASV..."))  # truncated payload

# 🔥 Insecure temp file
def unsafe_tempfile():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b"some secret stuff")

# 🔥 Hardcoded credentials
def leak():
    token = "ghp_1234567890abcdef"
    return token
