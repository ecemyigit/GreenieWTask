# Greenie Web Tech Intern Task

This is a Python script that monitors the CPU power usage of a specific process (identified by a PID). The script uses the `psutil` module to retrieve the necessary CPU usage data.

## Prerequisites

Before running this script, you need to have the following prerequisites:

- Python 3.x installed
- `psutil` module installed. If you don't have this module installed, use the following command to install it: `pip install psutil`

## Usage

1. Run the script with the command `python cpu_power_monitor.py`
2. Enter the PID of the process you want to monitor when prompted.
3. The script will start monitoring the CPU power usage of the process.
4. Press `Ctrl+C` to stop the monitoring.

## Script Explanation

1. Import the necessary modules:

```
import psutil
import time
import signal
import sys
```

2. Define a function to retrieve the Process object for a given PID:

```
def get_process_by_pid(pid):
    try:
        return psutil.Process(int(pid))
    except psutil.NoSuchProcess:
        print(f"Process with PID {pid} not found.")
        sys.exit(1)
```

3. Define a function to retrieve the CPU power usage data for a given Process object:

```
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
```

4. Check if the script is being run directly:

```
if __name__ == "__main__":
```

5. Retrieve the PID from the user:

```
pid = input("Enter PID of Application to be Monitored: ")
```

6. Retrieve the Process object for the specified PID:

```
process = get_process_by_pid(pid)
```

7. Start monitoring the CPU power usage of the process:

```
get_cpu_power_usage(process)
```
