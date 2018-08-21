<<<<<<< HEAD
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
=======
from flask import Flask, render_template, url_for, flash, redirect
>>>>>>> bf3186bfe795f48f82ab12b7de72bc56b08e1b1b
from forms import RegistrationForm, LoginForm
from models import User, Post

app = Flask(__name__)
app.config['SECRET_KEY'] = '86364228fcbf4f9217087814e08790ef'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)


posts = [
    {
        'author': 'Adia Chan',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 20, 2018'
    },
    {
        'author': 'Echo Li',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
