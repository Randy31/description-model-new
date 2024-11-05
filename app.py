from dotenv import load_dotenv
import os
import google.generativeai as genai
from flask import Flask, request, render_template

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the library with the API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Flask app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    generated_content = ""
    if request.method == 'POST':
        prompt = request.form.get('prompt')
        points = int(request.form.get('points', 5))
        if prompt:
            generated_content = generate_content(f"Write a product description in bullet points for '{prompt}' in {points} points")
    
    return render_template('index.html', generated_content=generated_content)

def generate_content(prompt):
    model = genai.GenerativeModel(model_name='gemini-pro')
    response = model.generate_content(prompt)
    result = response.text
    return result

if __name__ == '__main__':
    app.run(debug=True)
