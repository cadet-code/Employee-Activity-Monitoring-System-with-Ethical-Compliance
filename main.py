import tkinter as tk
from tkinter import messagebox, scrolledtext
from logger import log_system_usage
from privacy import store_secure_log
from reports import generate_compliance_report, generate_system_usage_report
from alerts import log_alerts

def login():
    user_id = user_id_entry.get()
    if user_id:
        activity = "User logged in"
        store_secure_log(user_id, activity)
        log_system_usage(user_id)
        messagebox.showinfo("Login", "User activity logged successfully.")
    else:
        messagebox.showwarning("Login", "User ID cannot be empty.")

def show_compliance_report():
    report = generate_compliance_report()
    report_window = tk.Toplevel(root)
    report_window.title("Compliance Report")
    report_text = scrolledtext.ScrolledText(report_window, wrap=tk.WORD, width=60, height=20)
    report_text.insert(tk.END, report)
    report_text.config(state=tk.DISABLED)
    report_text.pack(padx=10, pady=10)

def show_system_usage_report():
    report = generate_system_usage_report()
    report_window = tk.Toplevel(root)
    report_window.title("System Usage Report")
    report_text = scrolledtext.ScrolledText(report_window, wrap=tk.WORD, width=60, height=20)
    report_text.insert(tk.END, report)
    report_text.config(state=tk.DISABLED)
    report_text.pack(padx=10, pady=10)

def check_alerts():
    log_alerts()
    messagebox.showinfo("Alerts", "Alert check completed. See terminal for any alerts.")

# GUI Setup
root = tk.Tk()
root.title("Employee Activity Monitoring System")

# User ID Entry
user_id_label = tk.Label(root, text="User ID:")
user_id_label.grid(row=0, column=0, padx=10, pady=10)
user_id_entry = tk.Entry(root)
user_id_entry.grid(row=0, column=1, padx=10, pady=10)

# Buttons
login_button = tk.Button(root, text="Log Activity", command=login)
login_button.grid(row=1, column=0, columnspan=2, pady=10)

compliance_report_button = tk.Button(root, text="Show Compliance Report", command=show_compliance_report)
compliance_report_button.grid(row=2, column=0, columnspan=2, pady=10)

system_usage_report_button = tk.Button(root, text="Show System Usage Report", command=show_system_usage_report)
system_usage_report_button.grid(row=3, column=0, columnspan=2, pady=10)

alert_button = tk.Button(root, text="Check Alerts", command=check_alerts)
alert_button.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
