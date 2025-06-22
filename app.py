from flask import Flask, render_template, request, jsonify
import os
import openai  

app = Flask(__name__)

openai.api_key = os.getenv("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") 
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.json["message"]
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_response = response.choices[0].message["content"]
    except Exception as e:
        bot_response = f"MATRIX ERROR: {str(e)}" 

    return jsonify({"response": f"MATRIX: {bot_response}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
