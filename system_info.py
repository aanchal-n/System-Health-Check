import platform

def sys_details():
    uname=platform.uname()
    print("System:",uname.system)
    print("Node name:",uname.node)
    print("Release:",uname.release)
    print("Version:",uname.version)
    print("Machine:",uname.machine)
    print("Processor:",uname.processor)