from flask import Flask, render_template

app = Flask(__name__)

# Define a route for the landing page
@app.route('/')
def landing_page():
    # You can render an HTML template using Flask's render_template function
    return render_template('landing_page.html')

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
