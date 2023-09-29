import psutil
import time
import signal
import sys

def get_process_by_pid(pid):
    try:
        return psutil.Process(int(pid))
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
        sys.exit(1)

def get_cpu_power_usage(process, interval=1):
    start_time = time.time()
    start_energy = process.cpu_percent(interval=None)
    
    try:
        while True:
            time.sleep(interval)
            current_time = time.time()
            current_energy = process.cpu_percent(interval=None)
            
            # Calculate energy consumed based on CPU usage percentage
            energy_consumed = (current_time - start_time) * (current_energy / 100)
            
            print("{:,.4f} Joules of Energy Consumed.".format(energy_consumed))
    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
        sys.exit(0)

if __name__ == "__main__":
    pid = input("Enter PID of Application to be Monitored: ")
    process = get_process_by_pid(pid)
    get_cpu_power_usage(process)
