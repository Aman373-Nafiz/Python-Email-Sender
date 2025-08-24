import smtplib,ssl,getpass
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
My_Mail = 'azad85294@gmail.com'
Server_mail = 'smtp.gmail.com'
port = 587
password = input("Password:")
context = ssl.create_default_context()
mssg =MIMEMultipart()

try:
    server = smtplib.SMTP(Server_mail,port)
    server.starttls(context = context)
    server.login(My_Mail,password)
    print("Connection SuCCESful")
    Receptient_mail = input("Enter the mail address of receptient:")
    mssg['From'] = My_Mail
    mssg['To'] = Receptient_mail
    mssg['Subject'] = input("Subject ?")
    print("What is your message?")
    text_message = input().rstrip()
    mssg.attach(MIMEText(text_message))
    
    server.sendmail(My_Mail,Receptient_mail,mssg.as_string())
except:
    print("Connection Not succesful")

    
