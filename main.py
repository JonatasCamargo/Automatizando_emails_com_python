from email.message import EmailMessage
import smtplib
import ssl
import mimetypes

password = "* * * * * * * * * * *" #third-party app password for your gmail
from_email = "youremail@gmail.com"
to_email = "otheremail@gmail.com"

subject = 'Title'
body = open('files/index.html.txt', 'r', encoding='utf-8').read()

message = EmailMessage()
message['From'] = from_email
message['To'] = to_email
message['Subject'] = subject

message.set_content(body, subtype='html')
safe = ssl.create_default_context()

anexo = 'files/corpo.txt'
mime_type, mime_subtype = mimetypes.guess_type(anexo)[0].split('/')
with open(anexo, 'rb') as a:
    message.add_attachment(
        a.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=anexo
    )


with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=safe) as smtp:
    smtp.login(from_email, password)
    smtp.sendmail(
        from_email,
        to_email,
        message.as_string()
    )