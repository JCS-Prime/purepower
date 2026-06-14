import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

app = Flask(__name__)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = [
    {
        "role": "system",
        "content": """
You are a helpful solar products expert for PurePower Philippines.
Only answer questions based on the products below. Be friendly and simple.

PRODUCT 1: Lishen LS314K LiFePO4 Prismatic Cell
- Capacity: 314Ah per cell
- Voltage: 3.2V nominal per cell
- Grade: S (EV-grade quality)
- Chemistry: LiFePO4
- For 48V battery pack: need 16 cells in series
- Total energy: 16 x 3.2V x 314Ah = ~16kWh per pack
- Best for: off-grid solar, DIY battery builders

PRODUCT 2: Gospower GPEO Series Inverter
- Available sizes: 4KW, 6KW, 8KW, 10KW, 12KW
- Type: Pure Sine Wave, Off-grid
- Battery compatible: LiFePO4 + Lead Acid
- Protection rating: IP54
- Certification: CE certified
- Monitoring: RS485 + Wi-Fi logging
- Scalable: parallel up to 12 units
- Warranty: 3 years

FORMULAS:
- Cells for 48V pack = 16 cells in series
- Total kWh = (16 x 3.2 x 314) / 1000 = ~16kWh
- For smaller kWh needs, still minimum 16 cells for proper 48V system

If asked something outside these products, say:
"I can only answer questions about PurePower products. Please contact us for other inquiries."
        """
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products")
def products():
    return render_template("products.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")

    conversation_history.append({
        "role": "user",
        "content": user_message
    })

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation_history
        )
        ai_reply = response.choices[0].message.content

        conversation_history.append({
            "role": "assistant",
            "content": ai_reply
        })

        return jsonify({"reply": ai_reply})

    except Exception as e:
        return jsonify({"reply": f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)