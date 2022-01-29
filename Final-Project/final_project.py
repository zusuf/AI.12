import smtplib, ssl

port = 465
smtp_server = "smtp.gmail.com"

#LOGIN
sender_email = input(str("Your email: "))
password = input(str("Your password: "))

#RECEIVER LIST
with open('receiver_list.txt', 'r') as file:
  receiver_email = file.read().replace('\n', ',')

#MESSAGE
#Input
subject = input(str("Subject: "))
while len(subject)==0:
  print('Please fill the email Subject')
  subject = input(str("Subject: "))

body = input(str("Message: "))

#Message
message = f'Subject: {subject}\n\n{body}'

#SEND (SSL wrapper & send email)
try:
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    print("Email successfully sent!")
except Exception as exception:
  print("Error : %s!\n\n" % exception)


#Reference: 
# https://www.youtube.com/watch?v=MHAIjRhhn04
# https://www.youtube.com/watch?v=tZHCuA5Zug8
# https://www.youtube.com/watch?v=JRCJ6RtE3xU
# https://www.sololearn.com/Discuss/1582033/how-to-check-if-input-is-empty-in-python
# https://www.learnpython.org/en/String_Formatting