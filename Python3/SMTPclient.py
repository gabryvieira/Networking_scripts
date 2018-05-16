import smtplib

### SMTP client to send email from Gmail accounts
SMTP_PORT = 587


def main():
    smtp = smtplib.SMTP('smtp.gmail.com', SMTP_PORT)
    smtp.starttls()

    user_email = performLogin(smtp)
    sendEmail(smtp, user_email)


def performLogin(smtp):
    print("Login to your Gmail's account...")

    while True:
        username = input("Email: ")
        if username == "" or "@gmail" not in username:
            print("Invalid Gmail account!")
        else:
            break
    while True:
        password = input("Password: ")
        if password == "":
            print("Password cannot be empty!")
        else:
            break
    try:
        smtp.login(username, password)
    except smtplib.SMTPAuthenticationError:
        print("Username and Password not accepted!")
        exit()
    return username

def sendEmail(smtp, user_email):

    while True:
        msg = input("Type your message: ")
        if msg == "":
            print("Message cannot be empty!")
        else:
            break


    sendTo = input("Send email to: ")
    try:
        smtp.sendmail(user_email, sendTo, msg)
    except smtplib.SMTPRecipientsRefused:
        print("{} not a valid account!".format(sendTo))

if __name__ == '__main__':
    main()