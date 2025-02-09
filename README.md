# Windows Server Health Monitoring (Python + WMI)  

## Overview  
This project is designed to monitor critical system health metrics on a Windows server using Python and Windows Management Instrumentation (WMI). The script provides real-time insights into system performance, logs important data, and triggers alerts if predefined thresholds are exceeded.  

### Features:  
- **CPU Monitoring** – Tracks CPU usage and triggers alerts if it surpasses a defined threshold.  
- **Memory Monitoring** – Monitors RAM usage and sends alerts when excessive utilization is detected.  
- **Disk Monitoring** – Checks all disk drives and alerts if usage exceeds critical limits.  
- **Service Monitoring** – Ensures that essential services (e.g., DNS, DHCP) are running and not stopped.  
- **Logging & Alerts** – Saves all system metrics to a log file and sends email alerts when thresholds are exceeded.  

## Prerequisites  

### 1. Install Required Python Packages  
Ensure Python is installed, then install the necessary dependencies using:  
```
pip install wmi psutil
```

### 2. Run as Administrator  
Since WMI queries require elevated permissions, execute the script in an Administrator PowerShell or Command Prompt.  

## How the Script Works  

1. **CPU Monitoring** – Logs CPU usage and alerts if it exceeds the predefined threshold (default: 80%).  
2. **Memory Monitoring** – Monitors RAM utilization and sends alerts if it surpasses the limit (default: 80%).  
3. **Disk Monitoring** – Checks all disk partitions and alerts if any exceed the critical usage threshold (default: 90%).  
4. **Service Monitoring** – Verifies the status of critical Windows services (e.g., Windows Update, DNS Client, DHCP) and alerts if any are stopped.  
5. **Logging & Email Alerts** – Saves all system health metrics to a log file and sends email notifications if necessary.  

## How to Use the Script  

1. **Save the Script**  
   - Store the script as `server_monitor.py` in `C:\Scripts\`.  

2. **Modify Email Settings (Optional)**  
   - If email alerts are required, update the following variables:  
     - `SMTP_SERVER`, `SMTP_PORT`, `EMAIL_USERNAME`, `EMAIL_PASSWORD`, and `ALERT_EMAIL`.  
   - If email alerts are not needed, comment out the `send_alert()` function calls in the script.  

3. **Run the Script as Administrator**  
   - Open PowerShell with administrative privileges and execute:  
   ```
   python C:\Scripts\server_monitor.py
   ```

4. **Schedule Automatic Execution (Optional)**  
   - Open **Task Scheduler** in Windows.  
   - Create a new task that runs `python C:\Scripts\server_monitor.py` every hour or at a desired interval.  

## Next Steps & Improvements  

- **Expand Service Monitoring** – Add more critical Windows services based on your environment.  
- **Database Logging** – Store log data in a structured database instead of a plain text file.  
- **Visual Dashboard** – Integrate with monitoring tools like Grafana or Power BI for real-time visualization.  
