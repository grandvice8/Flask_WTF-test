from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.csrf import CSRFProtect
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log in")


app = Flask(__name__)
csrf = CSRFProtect(app)
Bootstrap(app)
app.secret_key = 'SomeSecretKey12345678'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == 'email@email.com' and login_form.password.data == 'password':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == "__main__":
    app.run(debug=True)