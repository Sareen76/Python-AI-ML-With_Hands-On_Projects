from flask import Flask, render_template, request

    # It creates an instance of the Flask class. 
    # which will be our WSGI application.

# WSGI Application
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about(): 
    return render_template('about.html')


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name}, Welcome to Flask Framework.'
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name=request.form['name']
    return f'Hello {name}, Welcome to Flask Framework.'

# Entry Point of any .py file is the main function.
if __name__ == '__main__':
    # sebug-True will act just same as nodemon or auto reload server
    app.run(debug=True)