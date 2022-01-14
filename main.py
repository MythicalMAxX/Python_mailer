import yagmail
import credentials

# mygmail = input("Enter your gmail address:")
# password = input("Enter your gmail password:")
"""You can remove the comments in order to get input by user"""


mygmail = credentials.gmail
password =  credentials.password
"""To secure my logins I used another file credentials.py and imported it"""

# receiver_mail = credentials.receivers_mail
"""You can also import reciver_mail by just removing above comment and adding recipients address in credentials.py """

print("Note: Due to google security issue you first need to turn on 'allow less secure apps access' from google security settings\n"
      "I recommend using alt gmail account as this code is for knowledge purpose only")


#reciever info
receiver_mail = input("Enter receiver mail:")
receiver_mail = receiver_mail.split()

# message content
subject = input("Enter the subject:")
body = input("Enter your message:")
attachment = input("Any attachments(y/n):")


#session login
yag = yagmail.SMTP(mygmail, password)

if attachment == "y":
    location = input("Enter filename along with extension\n"
                     " Or file path if file is not in same directory:")
    location = location.split()
    # converting file and file paths to list // note: files are split by space so make sure file name don't have space or it will return error

    try:
        yag.send(receiver_mail, subject, body,attachments=location)
        print("mail sent successfully")
    except :
        print("Something went wrong\n"
              " ***Possible Errors***\n"
              "1). Try checking you have allowed less secure apps access in google security settings\n"
              "2). Recheck your Gmail and Password\n"
              "3). Check your internet connection\n"
              "4). Check for attachement exists")
if attachment == "n":

    try:
        yag.send(receiver_mail, subject, body)
        print("mail sent successfully")
    except :
        print("Something went wrong\n"
              " ***Possible Errors***\n"
              "1). Try checking you have allowed less secure apps access in google security settings\n"
              "2). Recheck your Gmail and Password\n"
              "3). Check your internet connection")
