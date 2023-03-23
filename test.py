import psycopg2

conn = psycopg2.connect("dbname=practice user=leizhou")
cur = conn.cursor()
cur.execute('''select * 
                       from raw_transactions
                        ''') 






