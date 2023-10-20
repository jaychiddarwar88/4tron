import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendmail(receiver, subject, mailcontent):
    # mail_content = '''Hello,
    # This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
    # Thank You
    # '''

    #The mail addresses and password
    sender_address = '4tronstudios@gmail.com'
    sender_pass = 'vishwajeetjay123'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = '4tronstudios@gmail.com'
    message['Subject'] = subject   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mailcontent, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, '4tronstudios@gmail.com', text)
    session.quit()
    return "done"