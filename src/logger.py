import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.today().strftime('%Y%m%d')}.log"
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
if not os.path.exists(logs_path):
    os.makedirs(logs_path)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(filename=LOG_FILE_PATH,format='%(asctime)s %(levelname)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S',level=logging.INFO)

