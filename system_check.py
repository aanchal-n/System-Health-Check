import sys
import os
import hardware_check
import network_test
import software_update_check
import system_info
#import summary

print("*"*40,"This is a basic system health check", "*"*40)
print("\n")
print("BASIC SYSTEM INFORMATION")
system_info.sys_details()

dict_details={"cpu usage":0,
            "memory usage":0,
            "disk space":0,
            "update check":0,
            "network check":0}

print("\n HARDWARE CHECK")
print("\n CPU USAGE TEST")
dict_details["cpu usage"]=hardware_check.cpu_usage()
print("\n MEMORY USAGE TEST")
dict_details["memory usage"]=hardware_check.memory_usage()
print("\n DISK SPACE CHECK")
dict_details["disk space"]=hardware_check.disk_space_check()

print("\n UPDATE CHECK")
if sys.platform=="darwin":
    dict_details["update check"]=software_update_check.darwin_update()
else:
    dict_details["update check"]=software_update_check.linux_update()

print("\n NETWORK CHECK")
dict_details["network check"]=network_test.ping_check()

print("*"*40,"FINAL DIAGNOSTIC REPORT","*"*40)
print(dict_details)
#print("System Health Check Completed")
