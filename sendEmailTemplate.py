#!/usr/bin/python3.4
import email, smtplib, ssl
from datetime import date
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os


subject = "This is an automated script from Python that would be executed at 10:00 am IST daily"
body = "Please find the attachment of the RenewalCalculator file, and react !"
sender_email = "vishpython@gmail.com"
receiver_email = "vishvedula@gmail.com"
receiver_mail_list = ["vishvedula@gmail.com"]
#bcc_email = ["vishvedula@gmail.com","sravanthi.surya90@gmail.com"]
#password = input("Type your password and press enter:")


# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
#message["Bcc"] = bcc_email  # Recommended for mass emails
# Add body to email
message.attach(MIMEText(body, "plain"))


listItems = [
             ['Bike Pollution Check',date.today(),date(2021,3,21), 0],
             ['Car Insurance',date.today(),date(2021,4,23), 0],
             ['Washing Machine',date.today(),date(2022,2,19), 0],
             ['Bike Insurance',date.today(),date(2022,2,8), 0],
             ['Aquaguard AMC', date.today(), date(2021, 4, 15), 0],
             ['Paytm', date.today(), date(2021, 4, 15), 0]
            ]

renewaldatelist=[]

#Get the current working directory to save the file
cwd = os.getcwd()
#print(cwd)

save_path = cwd

notificationNeeded   = False


#Even before creating a new file , and sending via smtplib, we need to calculate the renewal Date

for i in range(0,len(listItems)):
        startdate = listItems[i][1]
        enddate = listItems[i][2]
        renewaldate = (enddate-startdate)
        listItems[i][3] = renewaldate.days
        renewaldatelist.append(renewaldate.days)

for i in range(0,len(renewaldatelist)):
    if renewaldatelist[i] <=1:
                notificationNeeded = True
                break




with open(os.path.join(save_path,'RenewalCalculator.txt'), 'w') as file1:
        for row in listItems: # for loop to add data into the text file
            file1.write(' || '.join([str(a) for a in row]) + '\n')



if(notificationNeeded):
    print('Your list contains a product which has either expired or going to expire soon')
    with open(file1.name, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        "attachment; filename= RenewalCalculator.txt",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        # here we need to make sure all the recipients get the mail
        for i in range(len(receiver_mail_list)):
            server.sendmail(sender_email, receiver_mail_list[i], text)
            #server.sendmail(sender_email, receiver_email, text)
    print('Please check your email , an attachment for the same has been sent')

else:
    print('No product with renewal date nearing 1 yet')

file1.close()
