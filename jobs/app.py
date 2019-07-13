from flask import Flask, render_template

# Create an instance of the Flask class called app
app = Flask(__name__)

# Route decorators
@app.route('/')
@app.route('/jobs')

# Index route function
def jobs():
    return render_template('index.html')
