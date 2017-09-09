import imaplib
import email

def email_get():
    username = 'dyganar@hotmail.com'
    password = 'tk982629'
    mail = imaplib.IMAP4_SSL('imap-mail.outlook.com')
    mail.login(username, password)

    result, mailboxes = mail.list()
    mail.select("inbox")

    result, data = mail.search(None, 'UNSEEN')
    i = 0
    msg = []
    for num in data[0].split():
        result, data = mail.fetch(num, '(BODY.PEEK[HEADER])')
        raw_email = data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        email_from = str(email.header.make_header(email.header.decode_header(email_message['from'])))
        email_subject = str(email.header.make_header(email.header.decode_header(email_message['subject'])))
        msg.insert(i,'Email {}: {} quer falar com você sobre {}'.format(i, email_from, email_subject))
        i+=1
    return msg
    mail.close()
    mail.logout()
