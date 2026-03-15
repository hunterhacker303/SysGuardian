import psutil
import os
import time

def process_analyzer(limit=5):
    processes = []

    for p in psutil.process_iter([ 'name', 'cpu_percent', 'memory_percent']):
        try:
            processes.append(p.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    
    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)


    print("----|Process Analyzer|----")
    print("CPU%\tMEM%\tNAME")
    print("-" * 27)

    for proc in processes[:limit]:
        print(f"{proc['cpu_percent']:.2f}\t{proc['memory_percent']:.2f}\t{proc['name']}")


while True:
    os.system("clear")
    process_analyzer()
    time.sleep(1)