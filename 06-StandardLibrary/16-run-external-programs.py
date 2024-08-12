import subprocess

# helper methods to work with Popen
# subprocess.call
# subprocess.check_call
# subprocess.check_output
# subprocess.Popen

# result = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
# result = subprocess.run(["python", "app.py"], capture_output=True, text=True)
try:
    result = subprocess.run(["false"],
                            capture_output=True,
                            text=True,
                            check=True)

    print(type(result))  # <class 'subprocess.CompletedProcess'>
    print("args", result.args)
    print("returncode", result.returncode)
    print("stderr", result.stderr)
    print("stdout", result.stdout)
except subprocess.CalledProcessError as ex:
    print("Hey error here")
    print(ex)

# if result.returncode != 0:
#     print(result.stderr)

# print(result.stdout)
