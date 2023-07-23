import sys
import logging
 
sys.path.insert(0, '/var/www/pi-server')
sys.path.insert(0, '/var/www/pi-server/venv/lib/python3.7/site-packages/')
 
# Set up logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# Import and run the Flask app
from app import app as application
