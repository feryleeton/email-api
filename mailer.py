import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from imap_tools import MailBox, AND


class Mailer:
    def __init__(self):
        self.context = ssl.create_default_context()

    @staticmethod
    def detect_smtp_server_by_login(email_address):
        if 'rambler.ru' in email_address:
            mail_server = 'smtp.rambler.ru'
            port = 465
        elif 'firstmail.ru' in email_address:
            mail_server = 'smtp.firstmail.ru'
            port = 465
        elif 'mail.ru' in email_address or 'inbox.ru' in email_address or 'bk.ru' in email_address:
            mail_server = 'smtp.mail.ru'
            port = 465
        else:
            mail_server = 'smtp.smartgridinsights.com'
            port = 465
        return mail_server, port

    @staticmethod
    def detect_imap_server_by_login(email_address):
        if 'rambler.ru' in email_address:
            imap_server = 'imap.rambler.ru'
        elif 'firstmail.ru' in email_address:
            imap_server = 'imap.firstmail.ru'
        elif 'mail.ru' in email_address or 'inbox.ru' in email_address or 'bk.ru' in email_address:
            imap_server = 'imap.mail.ru'
        else:
            imap_server = 'imap.smartgridinsights.com'

        return imap_server

    def send_email(self, send_from, send_to, subject, email_body, login, password):
        mail_server, port = self.detect_smtp_server_by_login(login)
        smtp_server = smtplib.SMTP_SSL(mail_server, port, context=self.context)
        smtp_server.ehlo()
        smtp_server.login(login, password)

        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Subject'] = subject

        msg.attach(MIMEText(email_body, 'plain'))

        text = msg.as_string()

        smtp_server.sendmail(send_from, send_to, text)
        smtp_server.close()
        print('Email sent !')

    def get_emails(self, filter_from, filter_to, login, password):

        imap_server = self.detect_imap_server_by_login(login)

        with MailBox(imap_server).login(login, password) as mailbox:
            if filter_to:
                messages = [msg for msg in mailbox.fetch() if msg.from_ == filter_from and msg.to[0] == filter_to]
            else:
                messages = [msg for msg in mailbox.fetch() if msg.from_ == filter_from]

            return messages
