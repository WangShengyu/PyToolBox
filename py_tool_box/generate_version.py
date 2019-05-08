import subprocess
import re
from py_tool_box import common

def extract_version(raw_version):
    m = re.search('VERSION_([0-9]*)_([0-9]*)-([0-9]*)-(.*)', raw_version)
    if m:
        return m.group(1) + "." + m.group(2), m.group(3)
    else:
        print ("Generate version fail. Can't find a tag like VERSION_X_X")
        return None

def get_version_by_tag():
    try:
        raw_version = common.get_cmd_output("git describe --tags --match VERSION_[0-9]*_[0-9]*")
    except Exception:
        return "", None
    version, subversion = extract_version(raw_version)
    if version == None:
        return "", None
    return version, subversion

def is_git_repo():
    try:
        get_output("git branch")
        return True
    except Exception:
        return False

def run():
    if not is_git_repo():
        return
    version, subversion = get_version_by_tag()
    if version == "":
        version = "0"
        subversion = common.get_cmd_output("git rev-list --count HEAD")
    commit = common.get_cmd_output("git log --format=%h -n 1")

    print(version + "." + subversion + "." + commit)

