# exploit.py

import os
import subprocess
import pickle
import base64
import tempfile

# 🔥 1. Command injection
def run_os_command(user_input):
    os.system("ping " + user_input)

# 🔥 2. Shell injection
def run_subprocess_command(user_input):
    subprocess.call("ping " + user_input, shell=True)

# 🔥 3. Unsafe deserialization
def deserialize_data():
    payload = b"gANjc3lzdGVtCkV4ZWN1dGUKcQApgXEBdS4="
    pickle.loads(payload)

# 🔥 4. Insecure temporary file creation
def unsafe_tempfile():
    tmp = tempfile.NamedTemporaryFile(delete=False)
    tmp.write(b"secret")
    tmp.close()

# 🔥 5. Hardcoded secret
def leaked_token():
    secret = "ghp_fakeHardcodedSecret_1234567890"
    return secret
