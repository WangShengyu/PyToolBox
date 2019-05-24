import subprocess
import re
import os
import shutil
from py_tool_box import common
from py_tool_box import generate_version
def run():
    if os.path.exists("debian") and os.path.isdir("debian"):
        shutil.rmtree("debian")
    if os.path.exists("build") and os.path.isdir("build"):
        shutil.rmtree("build")
    subprocess.run(["bloom-generate", "rosdebian", "--ros-distro", "melodic"])
    result = common.get_cmd_output("fakeroot debian/rules binary")
    result_lines = result.split("\n")
    last_line = result_lines[-1]
    m = re.search(".*building package '(.*)' in '(.*)'.", last_line)
    package_name = m.group(1)
    file_path = m.group(2)
    version = generate_version.generate_full_version()
    if version == None:
        version = "1.0"
    os.mkdir("build")
    shutil.move(file_path, "build/" + package_name + "_" + version + ".deb")
    
