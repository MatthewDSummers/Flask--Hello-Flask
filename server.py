from flask import Flask, render_template  # Import Flask to allow us to create our app
from string import capwords

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<name>') # for a route '/hello/____', anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    return "Hello, " + capwords(name)

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/repeat/<frequency>/<message>')
def repeat(message, frequency):
    frequency = int(frequency)
    message += " "
    result = frequency * message
    return result

@app.route('/html')
def index():
    return render_template("index.html")

if __name__=="__main__":
    app.run(debug=True)