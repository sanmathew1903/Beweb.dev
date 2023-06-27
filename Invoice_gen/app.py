from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_invoice():
    # Retrieve form data
    company_name = request.form['company_name']
    customer_name = request.form['customer_name']
    # Add more fields as per your requirements

    # Render the invoice HTML template with the provided data
    return render_template('invoice.html', company_name=company_name, customer_name=customer_name)