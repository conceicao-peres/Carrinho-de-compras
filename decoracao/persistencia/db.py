from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def connect_db():
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    passwd = os.environ.get('DB_PASSWD')
    db_name = os.environ.get('DB_NAME')

    url = 'mongodb+srv://' + user + ':' + passwd + host
    client = MongoClient(url)

    db = client[db_name]

    return db
