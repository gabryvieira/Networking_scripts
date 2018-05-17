import pexpect
from IPy import IP
import getpass
def main():

    session = "ftp "
    host = checkHostname()
    session += str(host)
    print(session)
    initSession(session)

def checkHostname():
    while True:
        host = input("Hostname: ")
        if host == "" or "." not in host:
            print("Input a valid IP address or domain")
        elif host.count('.') == 3:
            try:
                if IP(host):  # check if IP is valid (IPv6 included)
                    break
            except ValueError:
                print("Invalid IP address!")
                print("Values must be between 0 and 255!\n")
        else:
            break
    return host


def initSession(sessionFTP):
    ch = pexpect.spawn(sessionFTP)
    try:
        user = input("User: ")
        password = getpass.getpass("Password: ")
        ch.expect('Name .*:')
        ch.sendline(user)
        ch.expect('Password:')
        ch.sendline(password)
    except pexpect.exceptions.TIMEOUT:
        print("Timeout exceeded! Hostname, Username or Password may be wrong!")
        exit()
    print("Press any button to open session")
    ch.expect('ftp> ')
    print("Type help to show all available commands")
    ch.interact()   # interact manually

if __name__ == '__main__':
    main()






