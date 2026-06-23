from flask import Flask
app= Flask(__name__)

@app.route('/')
def home():
    return "Hello Students"


@app.route('/about')
def about():
    return "This is about page"

@app.route('/contact')
def contact():
    return "This is contact page"

@app.route('/details')
def details():
    return "This is details page"
"""
@app.route('/user/vishnu')
def user_vishnu():
    return 'Hello vishnu'
"""
# @app.route('/user/<name>')
# def user(name):
    # return f'Hello {name} welcome to my website'
# 
@app.route('/user/<name>/int:marks>')
def user_marks(name, marks):
    return f'Hello {name} your marks {marks}'


app.run(debug=True)