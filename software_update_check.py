import os
import sys

"""It runs a MacOS terminal comman to check for software. 
If updates are found, it prompts the user as to whether they want to install said updates manually or the code could install it for them""" 
def darwin_update():

    df_output_lines = [s.split() for s in os.popen("softwareupdate -l").read().splitlines()]

    if len(df_output_lines)<=3:
        print("No updates available")
        print("Moving on to next Check")
        return 0
    else:
        print("Updates Available")
        print("Enter Y for automatic updation")
        str_in="y"
        if str_in.lower()=="y":
            os.system("softwareupdate -a")  
            return 0
        else:
            return 1

"""The below code does the same as above but on a linux machine. 
Here we use sudo get-apt upgrade to check for updates and if available lets the user update the necessary software."""
def linux_update():

    df_output_lines = [s.split() for s in os.popen("bash software-update-linux.sh").read().splitlines()]
    main_list=df_output_lines[0]

    for i in range(0,len(main_list)):
        if main_list[i+1].lower()=="not" and main_list[i+2].lower()=="upgraded":
            print("Upgrade your software")
            return 1
            break
        else:
            print("Moving on to next check")
            return 0
            break



    
