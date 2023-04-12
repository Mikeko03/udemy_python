import smtplib, json


with open("login_info.json","r") as f:
    data = json.load(f)


gmail_user = data["gmail"]["email"]
gmail_pass = data["gmail"]["password"]


yahoo_user = data["yahoo"]["email"]
yahoo_pass = data["yahoo"]["password"]


connection = smtplib.SMTP("smtp.gmail.com")
#connection = smtplib.SMTP("smtp.mail.yahoo.com",port="587")
connection.starttls() #securing email connection
connection.login(user = gmail_user, password=gmail_pass)
#connection.login(user = yahoo_user, password=yahoo_pass)


try:
    connection.sendmail(from_addr=gmail_user, to_addrs=yahoo_user, msg="Hello2")
except:
    pass
else:
    print("email sent")

