import sys
import logging
 
sys.path.insert(0, '/var/www/pi-server')
sys.path.insert(0, '/var/www/pi-server/venv/lib/python3.7/site-packages/')
 
# Set up logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# Set dotenv
from dotenv import load_dotenv
project_folder = os.path.expanduser('/var/www/pi-server')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# Import and run the Flask app
from app import app as application
