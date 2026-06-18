import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from email_helper import send_email
from ai_helper import get_ai_reply

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/submit-inquiry", methods=["POST"])
def submit_inquiry():
    data = request.json
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    product = data.get("product")
    message = data.get("message")

    success = send_email(name, email, phone, product, message)

    if success:
        return jsonify({"status": "success", "message": "Inquiry sent!"})
    else:
        return jsonify({"status": "error", "message": "Something went wrong."})

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    ai_reply = get_ai_reply(user_message)
    return jsonify({"reply": ai_reply})

if __name__ == "__main__":
    app.run(debug=True)