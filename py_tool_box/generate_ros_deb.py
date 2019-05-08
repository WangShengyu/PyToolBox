import subprocess
def run():
    subprocess.run(["rm", "-rf", "debian"])
    subprocess.run(["bloom-generate", "rosdebian", "--ros-distro", "melodic"])
    subprocess.run(["fakeroot", "debian/rules", "binary"])
