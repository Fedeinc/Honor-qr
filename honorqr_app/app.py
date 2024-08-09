from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load OpenAI API key from environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/api/v1/chatbot', methods=['POST'])
def chatbot():
    data = request.get_json()
    message = data.get('message')
    context = data.get('context')

    if not message:
        return jsonify({'reply': 'Message is required'}), 400

    # Example response using OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": f"You are a helpful assistant. Context: {context}"},
                {"role": "user", "content": message}
            ]
        )
        reply = response.choices[0].message['content']
    except openai.error.OpenAIError as e:
        reply = f"OpenAI API error: {str(e)}"
    except Exception as e:
        reply = f"An error occurred: {str(e)}"

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for messages (for simplicity)
messages = []

@app.route('/')
def index():
    return render_template('tribute_wall.html', messages=messages)

@app.route('/send_message', methods=['POST'])
def send_message():
    message_text = request.form.get('message')
    if message_text:
        messages.append({
            'text': message_text,
            'time': 'Just now',
            'reactions': {'❤️': 0, '👍': 0, '😢': 0, '😊': 0}
        })
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
