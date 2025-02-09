import wmi
import psutil
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Define thresholds
CPU_THRESHOLD = 80  # Alert if CPU usage exceeds 80%
MEMORY_THRESHOLD = 80  # Alert if memory usage exceeds 80%
DISK_THRESHOLD = 90  # Alert if any disk usage exceeds 90%

# Log file path
LOG_FILE = "C:\\Users\\bboli\\dev\\Windows-Server-Health-Monitoring\\server_health.log"

# Email alert settings (optional)
ALERT_EMAIL = "admin@example.com"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587
EMAIL_USERNAME = "your-email@example.com"
EMAIL_PASSWORD = "your-email-password"

def write_log(message):
    """Logs messages with timestamps."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {message}\n"
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)
    print(log_entry.strip())  # Print to console as well

def send_alert(subject, body):
    """Sends an email alert when a threshold is exceeded."""
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USERNAME
    msg["To"] = ALERT_EMAIL

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, ALERT_EMAIL, msg.as_string())
        write_log(f"Alert sent: {subject}")
    except Exception as e:
        write_log(f"Failed to send alert: {str(e)}")

def check_cpu_usage():
    """Monitors CPU usage and logs if above threshold."""
    cpu_usage = psutil.cpu_percent(interval=1)
    write_log(f"CPU Usage: {cpu_usage}%")
    # if cpu_usage > CPU_THRESHOLD:
    #     send_alert("High CPU Usage Alert", f"CPU usage is at {cpu_usage}%!")

def check_memory_usage():
    """Monitors memory usage and logs if above threshold."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    write_log(f"Memory Usage: {memory_usage}%")
    # if memory_usage > MEMORY_THRESHOLD:
    #     send_alert("High Memory Usage Alert", f"Memory usage is at {memory_usage}%!")

def check_disk_usage():
    """Monitors disk usage and logs if any drive exceeds threshold."""
    for partition in psutil.disk_partitions():
        if "cdrom" in partition.opts or partition.fstype == "":
            continue  # Skip CD drives and unformatted partitions
        usage = psutil.disk_usage(partition.mountpoint)
        write_log(f"Disk {partition.device} Usage: {usage.percent}%")
        # if usage.percent > DISK_THRESHOLD:
        #     send_alert("High Disk Usage Alert", f"Disk {partition.device} is at {usage.percent}% usage!")

def check_services():
    """Checks the status of critical services like DNS and DHCP."""
    critical_services = ["wuauserv", "dnscache", "dhcp"]
    wmi_obj = wmi.WMI()
    for service in wmi_obj.Win32_Service():
        if service.Name.lower() in critical_services:
            status = "Running" if service.State == "Running" else "Stopped"
            write_log(f"Service {service.Name}: {status}")
            # if status == "Stopped":
            #     send_alert("Critical Service Stopped", f"The {service.Name} service is not running!")

def main():
    """Runs all monitoring functions and logs results."""
    write_log("=== System Health Check Started ===")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_services()
    write_log("=== System Health Check Completed ===")

if __name__ == "__main__":
    main()
