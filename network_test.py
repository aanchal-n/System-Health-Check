import os
import sys

def ping_check():
    df_output_lines = [s.split() for s in os.popen("bash ping-test.sh").read().splitlines()]
    main_list=df_output_lines[0]

    for i in range(0,len(main_list)):
        if main_list[i+1].lower()=="packet" and main_list[i+2].lower()=="loss":
            dummy=main_list[i]

            if sys.platform=="darwin":

                dummy=float(dummy[:len(dummy)-1])
                if dummy==0.0:
                    print("Your Network Connection is stable.")
                    return 0
                else:
                    print("Please test your network connection")
                    return 1

        
            else:
                dummy=int(dummy[:len(dummy)-1])
                if dummy==0:
                    print("Your network connection is stable")
                    return 0
                else:
                    print("Please check your network connetion")
                    return 1
            break
