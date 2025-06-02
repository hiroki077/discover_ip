Requirements
Linux (e.g., Ubuntu or other common distributions)

Python 3.x

pip (Python package manager)

Installing Dependencies
This script uses only the standard library and does not rely on any external packages. If you need additional libraries in the future, you can add them as required.

bash
コピーする
# Clone the repository
git clone https://github.com/hiroki077/discover_ip.git
cd <YourRepo>

# (Optional) Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# (At present, requirements.txt is not needed, but if you add packages later, use it)
pip install -r requirements.txt
Run the following in the terminal to edit your crontab:
bash
コピーする
crontab -e
Then add this line to schedule the Pico discovery script to run every day at 5:00 AM (closing all browser tabs before opening):

pgsql
コピーする
0 5 * * * /usr/bin/python3 /full/path/to/discover_ip.py >> /full/path/to/discover_ip.log 2