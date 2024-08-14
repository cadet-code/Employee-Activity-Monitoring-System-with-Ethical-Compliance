import sqlite3
import datetime

def check_suspicious_activity():
    conn = sqlite3.connect('activity_logs.db')
    c = conn.cursor()
    threshold_cpu = 80
    threshold_memory = 90
    c.execute('SELECT * FROM system_usage WHERE cpu_usage > ? OR memory_usage > ?', 
              (threshold_cpu, threshold_memory))
    alerts = c.fetchall()
    if alerts:
        for alert in alerts:
            print(f"ALERT: High system usage detected for User {alert[1]} at {alert[4]}")
    conn.close()

def log_alerts():
    # Run alert checks on a schedule or based on user activity
    check_suspicious_activity()
