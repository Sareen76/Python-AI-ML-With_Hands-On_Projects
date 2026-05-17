from flask import Flask

    # It creates an instance of the Flask class. 
    # which will be our WSGI application.

# WSGI Application
app = Flask()



# Enetery Point of any .py file is the main function.
if __name__ == '__main__':
    app.run()