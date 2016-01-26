from email.mime.text import MIMEText
msg = MIMEText('hellolili, send by Python~', 'plain', 'utf-8')

from_addr = 'mildwindyu@hotmail.com'#input('From: ')
password = 'cqhyf520'#input('Password: ')

to_addr = 'lzzsoul@sina.cn'#input('To: ')

smtp_server = 'smtp.live.com'#input('SMPT server: ')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.login(from_addr, password)
for i in range(20):
    server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
print('yes')
