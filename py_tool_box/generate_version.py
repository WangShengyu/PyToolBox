import subprocess
import re
from py_tool_box import common

def extract_version(version_tag):
    m = re.search('VERSION_([0-9]*)_([0-9]*)(.*)', version_tag)
    if m:
        return m.group(1) + "." + m.group(2)
    else:
        print ("Generate version fail. Can't find a tag like VERSION_X_X")
        return None

def get_version_by_tag():
    try:
        version_tag = common.get_cmd_output("git describe --tags --match VERSION_[0-9]*_[0-9]*")
    except Exception:
        return None
    version = extract_version(version_tag)
    if version == None:
        return None, None
    tag_commit = common.get_cmd_output("git rev-list -n 1 " + version_tag)
    subversion = common.get_cmd_output("git rev-list --count HEAD.." + tag_commit)
    return version, subversion

def is_git_repo():
    try:
        common.get_cmd_output("git branch")
        return True
    except Exception:
        return False

def generate_full_version():
    if not is_git_repo():
        return ""
    version, subversion = get_version_by_tag()
    if version == None:
        version = "0"
        subversion = common.get_cmd_output("git rev-list --count HEAD")
    commit = common.get_cmd_output("git log --format=%h -n 1")

    return version + "." + subversion + "." + commit

def run():
    print (generate_full_version())

