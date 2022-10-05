from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

def connect_db_produtos():
    host = os.environ.get('DB_HOST')
    user = os.environ.get('DB_USER')
    passwd = os.environ.get('DB_PASSWD')
    db_name = os.environ.get('DB_NAME')

    url = 'mongodb+srv://' + user + ':' + passwd + host
    produtos = MongoClient(url)

    db_produtos = produtos[db_name]

    return db_produtos



