from flask import Flask
from utils.invites import generate_invitation

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask app is running!"

@app.route('/generate')
def generate():
    return generate_invitation("Anish")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True, use_reloader=False)
