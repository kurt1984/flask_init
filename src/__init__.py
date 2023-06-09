from flask import Flask
import psycopg2
from src.model import Customer


def create_app(database, db_user):
    app = Flask(__name__)

    app.config.from_mapping(DATABASE = database, DB_USER= db_user)

    # breakpoint()
    @app.route("/")
    def index():
        return "hello!!"

    def db_connect():
        conn = psycopg2.connect(dbname=app.config['DATABASE'], user=app.config['DB_USER'])
        cur = conn.cursor()
        return cur


    @app.route("/customers/")
    def customers():
        cur = db_connect()
        cur.execute("select * from raw_transactions")        
        return [Customer(list).__dict__ for list in cur.fetchall()]

    @app.route("/customers/<id>")
    def customer_id(id):
        cur = db_connect()
        cur.execute('''select * 
                       from raw_transactions
                       where index = %s ''', (id,))        
        return Customer(cur.fetchone()).__dict__ 

    return app
