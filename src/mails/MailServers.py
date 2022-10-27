from src.mails.getting.schemes import MailServers


MailRu = MailServers(imap='imap.mail.ru', smtp='smtp.mail.ru')
Yandex = MailServers(imap='imap.yandex.com', smtp='smtp.yandex.com')

Gmail = MailServers(imap='imap.gmail.com', smtp='smtp.mail.ru')
Outlook = MailServers(imap='outlook.office365.com', smtp='smtp-mail.outlook.com', smtp_port=587)

