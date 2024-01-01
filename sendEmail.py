#10 minute mail for testpurpose =>https://10minutemail.com/
import smtplib

sendEmail=input("please enter the sender mail")
receiverMail=input("Enter the Sender mail")
msg=input("Enter the message")
password=input("Enter the password")

def sendEmail(sendEmail,receiverMail,password,msg):
    
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sendEmail,password)
        server.sendmail(sendEmail,receiverMail,msg)
        print("succesfully sent mail")
        server.close()
    
sendEmail(sendEmail,receiverMail,password,msg)
