from app_and_db import *
from urls import *

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    db.create_all()