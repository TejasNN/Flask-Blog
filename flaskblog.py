from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '35ca228704b446f3b028e8e2f65aa09c'
posts = [
    {
        'author': 'Jack willis',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted':  'March 21, 2024'
    },
    {
        'author': 'Mary Poppins',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted':  'March 21, 2024'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)
    
@app.route("/about")
def about():
    return render_template("about.html", title='About')
    
@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)
    
@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
    
if __name__ == '__main__':
    app.run(debug=True)