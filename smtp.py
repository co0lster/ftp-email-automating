import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def mail_send(postanowienia, mailpswd, login):
    fromaddr = login + "@zak.lodz.pl"
    toaddr = "all_meryt@zak.lodz.pl,all_tech@zak.lodz.pl"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = postanowienia.split('\n', 2)[1]
    body = postanowienia[1:]
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('212.191.91.98', 587)
    server.starttls()
    server.login(fromaddr, mailpswd)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr.split(","), text)
    server.quit()
