from src import create_app
from setting import database, db_user


app = create_app(database=database, db_user=db_user)

app.run(debug=True)