from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key ="org-nvZi8pbeDbI9f0wIoXzW4p5k"

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Matrix-themed AI. Talk like a robot from the future."},
            {"role": "user", "content": user_message}
        ]
    )
    return jsonify({"response": response.choices[0].message.content})

if __name__ == '__main__':
    app.run(debug=True)
