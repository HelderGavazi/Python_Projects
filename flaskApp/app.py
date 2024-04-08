from flask import Flask, render_template, request

# Create a Flask app instance
app = Flask(__name__)

# Define route for the landing page
@app.route('/')
def index():
    # Render the index.html template when accessing the root URL
    return render_template('index.html')

# Define route for the form submission
@app.route('/greet', methods=['POST'])
def greet():
    # Retrieve the name and email submitted through the form
    name = request.form['name']
    email = request.form['email']
    
    # Create a personalized greeting message
    greeting = f"Hello {name}! Your email is {email}."
    
    # Render the greet.html template with the personalized greeting
    return render_template('greet.html', greeting=greeting)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
