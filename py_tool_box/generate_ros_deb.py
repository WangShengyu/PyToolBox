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
    common.get_cmd_output("fakeroot debian/rules binary")
    dir_path = os.getcwd()
    package_name = os.path.basename(dir_path)
    deb_dir_path = os.path.join(dir_path, os.pardir)
    deb_files = [f for f in os.listdir(deb_dir_path) if os.path.isfile(os.path.join(deb_dir_path, f)) and f[-4:] == ".deb"]
    file_path = os.path.join(deb_dir_path, deb_files[0])
    version = generate_version.generate_full_version()
    if version == None:
        version = "1.0"
    os.mkdir("build")
    shutil.move(file_path, "build/" + package_name + "_" + version + ".deb")
    
