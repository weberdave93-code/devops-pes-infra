import os
import time

def clean_expired_logs(log_dir="./logs", days=7):
    os.makedirs(log_dir, exist_ok=True)
    for i in range(5):
        with open(f"{log_dir}/app{i}.log", "w") as f:
            f.write(f"test log {i} - {time.ctime()}")
    now = time.time()
    for file in os.listdir(log_dir):
        if file.endswith(".log"):
            file_path = os.path.join(log_dir, file)
            modify_time = os.path.getmtime(file_path)
            if now - modify_time > days * 86400:
                os.remove(file_path)
                print(f"Deleted expired log: {file_path}")
    print("Log clean completed!")

if __name__ == "__main__":
    clean_expired_logs()
