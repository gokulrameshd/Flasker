from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

#create a flask instance
app = Flask(__name__)

# CSFR 
app.config['SECRET_KEY'] = "my super secret key that no one supposed to know"

# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's your name" , validators = [DataRequired()])
    submit = SubmitField("Submit")
    # BooleanField
    # DateField
    # DecimalField
    # FileField
    # HiddenField
    # MultipleField
    # FloatField
    # FromField
    # IntegerField
    # PasswordField
    # RadioField
    # URL
    # UUID
    # IP



# Create a route decorator
@app.route("/")

# def index():
#     return "<h1>Hello World!</h1>"


# Filters:::: '''
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags
# '''

def index():
    first_name = "John"
    stuff = "This is bold text"
    favorite_pizza = ["Pepperoni","Cheese","41"]
    return render_template("index.html",
                            first_name=first_name,
                            stuff=stuff,
                            favorite_pizza=favorite_pizza)

# localhost:5000/user/John
@app.route("/user/<name>")

def user(name):
    return render_template("user.html", user_name= name)

# Create Custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Intrernal server Error Thing
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name Page
@app.route("/name",methods = ['GET','POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form submitted successfully!!")
    return render_template("name.html",
                            name = name,
                            form = form)