from flask import Flask, render_template

    # It creates an instance of the Flask class. 
    # which will be our WSGI application.

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about(): 
    return render_template('about.html')

# Entry Point of any .py file is the main function.
if __name__ == '__main__':
    # sebug-True will act just same as nodemon or auto reload server
    app.run(debug=True)