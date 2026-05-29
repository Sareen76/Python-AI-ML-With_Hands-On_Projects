### Jinja2 is a template engine for Python. It is used to create dynamic web pages by allowing you to embed Python code within HTML templates. Jinja2 provides a powerful and flexible way to generate HTML content based on data and logic defined in your Python code.
# {{}} expression to print output in html
# {% %} expression to write logic in html
# {#..#} expression to write comments in html


from flask import Flask, render_template, request



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


@app.route('/submit', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        name=request.form['name']
        return f'Hello {name}, Welcome to Flask Framework.'
    return render_template('form.html')

## Variable Rule
@app.route('/success/<int:score>', methods=['GET'])
def success(score):
    return f"The marks You got is {score}"



## Bulding URL dynamically
@app.route('/result/<int:score>', methods=['GET', 'POST'])
def result(score):
    res=""
    if score >= 50:
        res="You are Passed"
    else:
        res="You are Failed"
    exp={'score':score, 'result':res}
    return render_template('result.html', data=exp)







# Entry Point of any .py file is the main function.
if __name__ == '__main__':
    # sebug-True will act just same as nodemon or auto reload server
    app.run(debug=True)