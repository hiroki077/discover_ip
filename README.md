# discover_ip

A Python script that discovers a Raspberry Pi Pico on the local network via UDP broadcast, closes all existing browser tabs, and then opens the Pico’s web interface in the default browser. Includes instructions for scheduling the script to run every day at 5:00 AM using cron.

---

## Overview

- **Purpose**  
  - Automatically detect a Raspberry Pi Pico on the local network and launch its web interface.  
  - Close any open browser tabs before opening the Pico’s interface to ensure it appears front and center.  
  - Provide a cron configuration example so that the script runs at a fixed time (5:00 AM) every day.

---

## Requirements

- **Operating System**  
  - Linux (e.g., Ubuntu or other common distributions)  

- **Python**  
  - Python 3.x  
  - This script relies only on the standard library, so no external packages are required by default.  

- **pip** (optional)  
  - Only needed if you plan to add additional dependencies in the future.  

- **X11 or Wayland Session**  
  - If you plan to launch the browser from cron, the system must have an active graphical session or you must export the `DISPLAY` environment variable so the browser can start.  

---

## Installation

1. **Clone the repository**  
    ```bash
    git clone https://github.com/hiroki077/discover_ip.git
    cd discover_ip
    ```

2. **(Optional) Create and activate a virtual environment**  
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**  
   - Currently, no external packages are needed. If you add any libraries later, install them with:
    ```bash
    pip install -r requirements.txt
    ```

4. **Make the script executable**  
    ```bash
    chmod +x discover_ip.py
    ```

---

## Scheduling with cron

To run the Pico discovery script automatically every day at 5:00 AM, add a cron entry as follows. Replace paths with those that match your environment.

1. Open your crontab:
    ```bash
    crontab -e
    ```

2. Add this line:
    ```cron
    0 5 * * * export DISPLAY=:0 && /usr/bin/python3 /full/path/to/discover_ip.py >> /full/path/to/discover_ip.log 2>&1
    ```
    - `0 5 * * *` → run every day at 5:00 AM  
    - `export DISPLAY=:0` → ensure the script can launch a graphical browser (adjust if you use Wayland or a different display)  
    - `/usr/bin/python3` → path to your Python 3 interpreter (`which python3` can tell you)  
    - `/full/path/to/discover_ip.py` → absolute path to the script in this repository  
    - `>> /full/path/to/discover_ip.log 2>&1` → append both standard output and standard error to a log file. Remove the redirection if you do not need logs.

---

## Usage

### Manual Execution

```bash
python3 discover_ip.py
