import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sendersemail@gmail.com','password')
server.sendmail('sendersemail@gmail.com','recieversemail.com','text message')
