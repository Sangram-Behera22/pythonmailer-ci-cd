import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import os

def send_mail(workflow_name,repo_name,workflow_run_id):
    sender_mail = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')
    receiver_email = os.getenv('RECEIVER_EMAIL')

    subject = f"workflow {workflow_name} failed for repo {repo_name}"
    body = f"Hi, the workflow {workflow_name} failed for the repo {repo_name}. Please check the logs for more details.\n More Details: \nRun_ID: {workflow_run_id}"

    msg= MIMEMultipart()
    msg['From'] = sender_mail
    msg['To']= receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body,'plain'))

    try:
       server = smtplib.SMTP('smtp.gmail.com',587)
       server.starttls()
       server.login(sender_mail,sender_password)
       text = msg.as_string()
       server.sendmail(sender_mail,receiver_email,text)
       server.quit()
       print('Email sent successfully')
    except Exception as e:
       print(f"Error:{e}")