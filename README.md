# webmonstack
Web site / Web application monitoring using Prometheus, BlackBox Exporter, Grafana



# Installation
1. Install Docker and Docker Compose 
2. clone the repository
3. Updated values on below files
   - webmonstack/prometheus/blackbox_targets.yml 
      Configure web URLs and update the group labels
   - webmonstack/alertmanager/config.yml 
      Configure sendgrid API key and Email address
   - webmonstack/proxy/.htpasswd
      Update htaccess credentials
   - webmonstack/scripts/prom-web-availability.py
      Update Prometheus URL, sender and receiver email addresses 
4. Configure cronjob to run the script *"webmonstack/scripts/prom-web-availability.py"* on 1st of every month
5. docker compose up -d 

# Grafana Dashboards
### Web-Overview
![Overview](https://github.com/iquzart/webmonstack/blob/master/images/web-overview.png)
### Web-Availability
![Availablibilty](https://github.com/iquzart/webmonstack/blob/master/images/web-Availability.png)

# Email Notification - Monthly Availability
### HTML Email Sample
![EmailReport](https://github.com/iquzart/webmonstack/blob/master/images/Email%20Report%20-%20Availability.PNG)

