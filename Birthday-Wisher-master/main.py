import pandas as pd
import datetime
import smtplib
import os

# Email id and password
GMAIL_ID=''
GMAIL_PSWD=''

def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject: {sub} and message {msg}" )
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(GMAIL_ID, GMAIL_PSWD)
    s.sendmail(GMAIL_ID, to, f"Subject: {sub}\n\n{msg}")
    s.quit()


if __name__=='__main__':
    df=pd.read_excel('Details.xlsx')
    # print(df)
    today=datetime.datetime.now().strftime('%d-%m')
    # print(today)
    # print(type(today))

    for index,item in df.iterrows():
        # print(index,item['Birthday'])
        bday=item['Birthday'].strftime('%d-%m')
        # print(bday)
        print(today,'  ',bday)

        if(today==bday):
            sendEmail(item['Email'],"Happy birthday",item['Dialogue']);        
