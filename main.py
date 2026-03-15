import time
import psutil
import os

def display_usage(cpu_usage, mem_usage,disk_usage, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '#' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    mem_percent = (mem_usage / 100.0)
    mem_bar = '#' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))

    disk_percent=(disk_usage / 100.0)
    disk_bar='#'*int(disk_percent*bars) +'-'*(bars-int(disk_percent *bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}% ")

    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}% ")

    print(f"Disk Usage: |{disk_bar}| {disk_usage:.2f}% ")



while True:
    os.system("clear")
    display_usage(psutil.cpu_percent(), psutil.virtual_memory().percent,psutil.disk_usage('/').percent ,30)
    
    time.sleep(0.5)
