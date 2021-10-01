import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(to, subject, text):

    from_email = 'asdmalizia@gmail.com'
    psw = 'm8007a6524'

    smtp_server = 'smtp.gmail.com'
    port = 587

    context = ssl.create_default_context()

    try:
        session = smtplib.SMTP(smtp_server, port)
        session.starttls(context=context)
        session.login(from_email, psw)

        message = MIMEMultipart()
        message['From'] = 'Defacement Report'
        message['Subject'] = subject
        message['To'] = to
        
        message.attach(MIMEText(text, 'plain'))

        session.sendmail(from_email, to, message.as_string())
    except Exception as e:
        print(f'Error: {e}')
    
    finally:
        session.quit()


send_email('alessandramalizia@hotmail.com', 'PFC Notification', 'testing')


