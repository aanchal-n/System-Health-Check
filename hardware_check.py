import os
import sys
import subprocess
import re

"""Below function uses a basic shell command to extract the cpu stats.
The shell command uses pf and pipes it to an awk command.
Based on the computed percentage, It prompts the user on the status."""

def cpu_usage():
    dir=os.popen("bash cpu_usage.sh").readline()
    cpu_percent=float(dir[:len(dir)-2])
    if cpu_percent>=95.0:
        print("Your cpu is approaching Maximum usage. Kindly close applications")
        return 1
    else:
        print("Your cpu is at normal usage")
        print("Moving on to next check")
        return 0

"""The below function is divided into two halves.
The first half utilisese subprocess to obtain the stats of the ram usage on a MacOS machine.
The Second half utilises the shell command free to obtain stats of a linux machine.
It finally gives an output based on the percentage of ram used."""

def memory_usage():

    stats={}
    if sys.platform=="darwin":
        matcher = re.compile('\d+')

        total_ram = subprocess.run(['sysctl', 'hw.memsize'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode('utf-8')
        vmLines = vm.split('\n')

        wired_memory = (int(matcher.search(vmLines[6]).group()) * 4096) / 1024 ** 3
        free_memory = (int(matcher.search(vmLines[1]).group()) * 4096) / 1024 ** 3
        active_memory = (int(matcher.search(vmLines[2]).group()) * 4096) / 1024 ** 3
        inactive_memory = (int(matcher.search(vmLines[3]).group()) * 4096) / 1024 ** 3

        stats["total_ram"]=int(matcher.search(total_ram).group())/1024**3
        stats["used_ram"]=round(wired_memory+active_memory+inactive_memory, 2)
    else:
        df_output_lines = [s.split() for s in os.popen("bash memory_check.sh").read().splitlines()]
        ram_details=df_output_lines[0]

        stats["total_ram"]=int(ram_details[1])
        stats["used_ram"]=int(ram_details[2])

    ram_percent=(stats["used_ram"]/stats["total_ram"]*100) 
    if ram_percent>=95.0:
        print("Your ram consumption is high. Close applications")
        return 1
    else:
        print("Your ram consumption is optimal")
        print("Moving on to next check")
        return 0

"""The below method checks for the disk space occupied on a system. 
It runs different shell commands for the two different os's owing to the different names of the drives.
The percentage is computed and tested"""

def disk_space_check():

    dict_rec={}

    if sys.platform=="darwin":
        df_output_lines = [s.split() for s in os.popen("bash disk-space-macos.sh").read().splitlines()]
    else:
        df_output_lines = [s.split() for s in os.popen("bash disk-space-linux.sh").read().splitlines()]

    dict_rec["total_space"]=float(df_output_lines[0][1][:-2])
    dict_rec["used_space"]=float(df_output_lines[0][2][:-2])
    dict_rec["available_space"]=float(df_output_lines[0][3][:-2])
    dict_rec["percent_free"]=round((dict_rec["available_space"]/dict_rec["total_space"])*100,2)
    
    if dict_rec["percent_free"]<=5.0:
        print("You are running low on disk space")
        return 1
    else:
        print("Your system has enough disk space")
        print("Moving on to next check")
        return 0
