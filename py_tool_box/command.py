import sys
from py_tool_box import generate_version
from py_tool_box import generate_ros_deb

tool_list = {
    "gv": {
        "func": generate_version.run,
        "desc": "Generate version by git info"
    }
    , "grd": {
        "func": generate_ros_deb.run,
        "desc": "Generate debian from a ros package"
    }
}

def help():
    print ("usage: pytoolbox toolname\n");
    print ("tool name list:\n")
    for k, v in tool_list.items():
        print("%10s : %s" % (k, v["desc"]))

def run():
    if len(sys.argv) < 2 or not sys.argv[1] in tool_list:
        help()
        exit()
    tool_name = sys.argv[1]
    # remove tool_box from argv
    sys.argv = sys.argv[1:]

    tool_list[tool_name]["func"]()
