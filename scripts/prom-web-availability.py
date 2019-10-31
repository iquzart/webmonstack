#/usr/bin/python3
import requests
import simplejson as json
from jinja2 import Environment, FileSystemLoader
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime

# Variables
Prometheus_URL = 'http://prometheus:9090/'
sender = 'notification@domain'
receiver = 'email'


def promapi():
    """
    Retun Prometheus query result in HTML
    """
   
    report_date = datetime.today().strftime('%B %Y')
    duration = '[' + str(24) + 'h]'
    response = requests.get(Prometheus_URL + '/api/v1/query',
      params={
        'query': 'avg_over_time(probe_success'+ duration +')*100'
        }) 
    data = json.loads(response.text)
    length_of_values = (len(data['data']['result']))
    group = []
    instance = []
    availability = []
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    template = env.get_template('report.html')

    for id in range(length_of_values):
        metric = (data['data']['result'][id]['metric'])
        availability.append(round(float(data['data']['result'][id]['value'][1]),2))
        group.append(metric['groups'])
        instance.append(metric['instance'])

    body = template.render(report_date=report_date, instance_group_availability=zip(instance,group,availability))
    return body

def main():
    """
    Send Availability report in HTML format
    """
    
    body = promapi()
    msgRoot = MIMEMultipart('alternative')
    msgRoot['Subject'] = 'Availability Report'
    msgRoot['From'] = sender
    msgRoot['To'] = receiver
    msgRoot.attach(MIMEText(body, 'html'))

    
    try:
       smtpObj = smtplib.SMTP('localhost')
       smtpObj.sendmail(sender, receiver, msgRoot.as_string())
       smtpObj.quit()
       print ("Successfully sent email")
    except:
       print ("There was an error sending the email. Check the smtp settings.")

main()

