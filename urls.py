from app_and_db import app
from flask import redirect, url_for, render_template


@app.route('/')
def home_page():
    return redirect(url_for('login'))


@app.route('/login/')
def login():
    return render_template('/login.html')


@app.route('/sign-in/')
def sign_in():
    return render_template('/sign-in.html')


if __name__ == '__main__':
    app.run(debug=True)
    from app_and_db import db
    db.create_all()



