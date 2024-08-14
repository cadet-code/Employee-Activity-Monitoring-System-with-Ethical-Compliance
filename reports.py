import sqlite3

def generate_compliance_report():
    conn = sqlite3.connect('activity_logs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM logs')
    logs = c.fetchall()
    report = "Compliance Report\n\n"
    report += "User ID | Activity | Timestamp\n"
    report += "-"*40 + "\n"
    for log in logs:
        report += f"{log[1]} | {log[2]} | {log[3]}\n"
    conn.close()
    return report

def generate_system_usage_report():
    conn = sqlite3.connect('activity_logs.db')
    c = conn.cursor()
    c.execute('SELECT * FROM system_usage')
    usage_logs = c.fetchall()
    report = "System Usage Report\n\n"
    report += "User ID | CPU Usage | Memory Usage | Timestamp\n"
    report += "-"*50 + "\n"
    for log in usage_logs:
        report += f"{log[1]} | {log[2]}% | {log[3]}% | {log[4]}\n"
    conn.close()
    return report
