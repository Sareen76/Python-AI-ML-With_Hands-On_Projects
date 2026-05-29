from flask import Flask

    # It creates an instance of the Flask class. 
    # which will be our WSGI application.

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Flask Framework. This should be an amazing course.'

@app.route('/about')
def about():
    return 'About Page'

# Entry Point of any .py file is the main function.
if __name__ == '__main__':
    # sebug-True will act just same as nodemon or auto reload server
    app.run(debug=True)