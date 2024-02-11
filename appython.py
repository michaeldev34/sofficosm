from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# Define route for the home page
@app.route('/')
def home():
    return 'Welcome to My Flask App!'

# Define route for a sample endpoint
@app.route('/hello')
def hello():
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
