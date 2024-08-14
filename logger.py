import psutil
import datetime
import sqlite3

def log_activity(user_id, activity):
    conn = sqlite3.connect('activity_logs.db')
    c = conn.cursor()
    timestamp = datetime.datetime.now()
    c.execute('INSERT INTO logs (user_id, activity, timestamp) VALUES (?, ?, ?)', 
              (user_id, activity, timestamp))
    conn.commit()
    conn.close()

def log_system_usage(user_id):
    conn = sqlite3.connect('activity_logs.db')
    c = conn.cursor()
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    timestamp = datetime.datetime.now()
    c.execute('INSERT INTO system_usage (user_id, cpu_usage, memory_usage, timestamp) VALUES (?, ?, ?, ?)', 
              (user_id, cpu_usage, memory_usage, timestamp))
    conn.commit()
    conn.close()

# Initialize the database
def init_db():
    conn = sqlite3.connect('activity_logs.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    activity TEXT NOT NULL,
                    timestamp DATETIME NOT NULL
                 )''')
    c.execute('''CREATE TABLE IF NOT EXISTS system_usage (
                    id INTEGER PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    cpu_usage REAL NOT NULL,
                    memory_usage REAL NOT NULL,
                    timestamp DATETIME NOT NULL
                 )''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
