from dotenv import load_dotenv
import os

load_dotenv()

database = os.getenv('DATABASE')
db_user = os.getenv('DB_USER')