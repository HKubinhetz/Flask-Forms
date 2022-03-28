# ------------------------------------- IMPORTS -----------------------------------------
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


# ------------------------------------ CONSTANTS ----------------------------------------
# Some example login info to validate your credentials down the line (see "login" function)
good_login = "admin@email.com"
good_pass = "12345678"


# ----------------------------------- FORM CREATION -------------------------------------
class MyForm(FlaskForm):
    # Mail input field
    mail = StringField(label='E-mail:',
                       validators=[DataRequired(), Email()])

    # Password input field
    password = PasswordField(label='Password:',
                             validators=[DataRequired(), Length(min=8)])

    # Submit button
    submit = SubmitField(label='Log In',
                         validators=[DataRequired()])


# ----------------------------------- FLASK SERVER --------------------------------------
# Creating a Flask Server
app = Flask(__name__)
Bootstrap(app)


# If route is "root", render index.html:
@app.route("/")
def home():
    return render_template('index.html')


# If route is localhost/login, flask renders different pages depending on the method:

# GET happens when a client accesses the login page.
# GET renders 'login.html'

# POST happens when a client submits the form.
# POST renders 'old_success.html'/'denied.html', whether the correct credentials were provided

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm(meta={'csrf': False})
    if form.validate_on_submit():
        if form.mail.data == good_login and form.password.data == good_pass:
            # Good Login!
            return render_template('success.html')
        else:
            # Bad Login!
            return render_template('denied.html')
    return render_template('login.html', form=form)


# --------------------------------- RUNNING THE SITE ------------------------------------
if __name__ == '__main__':
    app.run(debug=True)
