import psutil
import os
import time

psutil.cpu_percent(interval=None)
def get_top_process():

    top_process = "Unknown"
    max_cpu = 0
    max_mem = 0

    for p in psutil.process_iter(['name', 'memory_info', 'cpu_percent']):
        try:
            cpu = p.info['cpu_percent'] or 0
            mem = p.info['memory_info'].rss if p.info['memory_info'] else 0

            if cpu > max_cpu:
                max_cpu = cpu
                top_process = p.info['name']

            if mem > max_mem:
                max_mem = mem

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

    mem_gb = max_mem / (1024 ** 3)

    return top_process, max_cpu, mem_gb


def smart_diagnosis():

    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    process_name, process_cpu, process_mem = get_top_process()

    print("\n===== SMART SYSTEM DIAGNOSIS =====\n")

    # CPU Check
    if cpu > 80:
        print("Warning: High CPU usage detected\n")
        print(f"Top process: {process_name}")
        print(f"CPU usage: {process_cpu:.2f}%\n")
        print("Suggested action:")
        print("Close heavy applications\n")

    # RAM Check
    elif memory > 80:
        print("Warning: High RAM usage detected\n")
        print(f"Top process: {process_name}")
        print(f"Memory usage: {process_mem:.2f}GB\n")
        print("Suggested action:")
        print("Close unused tabs or restart browser\n")

    # Disk Check
    elif disk > 90:
        print("Warning: Disk space almost full\n")
        print(f"Disk usage: {disk:.2f}%\n")
        print("Suggested action:")
        print("Delete unnecessary files\n")

    else:
        print("System running normally\n")


while True:

    os.system("cls")

    smart_diagnosis()

    time.sleep(2)