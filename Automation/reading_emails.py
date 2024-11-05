import smtplib

conn = smtplib.SMTP('smtp.gmail.com',587)
print(type(conn))

print(conn.ehlo())

print(conn.starttls())

print(conn.login('siddharthnm07@gmail.com','wiim uowt nuwa kbhn'))

print(conn.sendmail('siddharthnm07@gmail.com','siddharthnm07@gmail.com','Subject: Demo email....\n\n Hi Siddu , How are u doing? \n\n -Siddharth'))

print(conn.quit())
