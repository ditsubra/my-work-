import smtplib

email = input ('SENDER EMAIL:')
receiver_email = input('RECEIVER EMAIL:')

subject = input ('subject :')
message = input ('message :')

text = f"subject: {subject}\n\n{message}"

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login(email,'kuwjzylvcmnrsjgt')

server.sendmail(email,receiver_email,text)

print("Email has been sent to" + receiver_email)
