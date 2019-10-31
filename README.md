# webmonstack
Web site / Web application monitoring using Prometheus, BlackBox Exporter, Grafana



# installation
1. install Docker and Docker Compose 
2. Updated values on below files
   - webmonstack/prometheus/blackbox_targets.yml 
   - webmonstack/alertmanager/config.yml 
   - webmonstack/proxy/.htpasswd
   - webmonstack/scripts/prom-web-availability.py
   - 

# Grafana Dashboards
![Overview](https://github.com/iquzart/webmonstack/blob/master/images/web-overview.png)
![Availablibilty](https://github.com/iquzart/webmonstack/blob/master/images/web-Availability.png)

# Email Notification - Monthly Availability
![EmailReport](https://github.com/iquzart/webmonstack/blob/master/images/Email%20Report%20-%20Availability.PNG)

