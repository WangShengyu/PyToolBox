import subprocess
def get_cmd_output(cmd):
    cmd_arr = cmd.split(" ")
    return subprocess.check_output(cmd_arr).decode().rstrip()

