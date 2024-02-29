import smtplib
from email import encoders
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
def mailreport():
    fromaddres = "aketo1337@mail.ru"
    toaddr = "aketo1337@mail.ru"
    mypass = "pytest"
    reportname = "log.txt"

    msg = MIMEMultipart()
    msg['From'] = fromaddres
    msg['To'] = toaddr
    msg['Subject'] = "Hello bratik"
    print(123)
    with open(reportname, "rb") as f:
        part = MIMEApplication(f.read(), Name=basename(reportname))
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(reportname)
        msg.attach(part)
    body = "Chekidout"
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.mail.ru', 587)

    server.starttls()
    server.login(fromaddres, mypass)
    text = msg.as_string()
    server.sendmail(fromaddres, toaddr, text)
    server.quit()
print("tut")