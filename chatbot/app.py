from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv
load_dotenv()


app = Flask(__name__)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def query_groq_cloud(user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a helpful movie suggestion bot. "
                    "Your ONLY job is to recommend movies based on genre, mood, or language. "
                    "If the user asks anything else, reply: 'I'm only trained to suggest movies. 😊'"
                )
            },
            {
            "role": "user",
            "content": user_input
        }    ]
    }

    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    print(result)
    return result

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json() 
        user_input = request.form.get("message") 

        response = query_groq_cloud(user_input)
        reply = response['choices'][0]['message']['content']

        return jsonify({'reply': reply})
    except Exception as e:
        print("Error:", e)
        return jsonify({'reply': "Sorry, something went wrong on the server 😓"}), 500

if __name__ == "__main__":
    app.run(debug=True)
