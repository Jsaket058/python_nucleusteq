# 8. Implement a program that creates a log file with timestamped entries

from datetime import datetime

def write_log(message, log_file='file_handling/app.log'):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"[{timestamp}] {message}\n"
    
    with open(log_file, 'a') as file:
        file.write(entry)


write_log("hey there , its started")
write_log("I am logged in")
write_log("Byee")
