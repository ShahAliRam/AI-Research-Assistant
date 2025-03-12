from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Sample responses - in a real app, you would integrate with an actual AI model
def get_ai_response(message):
    # This is a placeholder - in a real application, you would connect to an AI model API
    return f"I received your message: '{message}'. This is a simulated response from the AI Research Assistant."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    
    print(data)

    if not message:
        return jsonify({'error': 'No message provided'}), 400
    
    response = get_ai_response(message)
    
    return jsonify({
        'response': response,
        'timestamp': datetime.now().strftime('%H:%M')
    })

if __name__ == '__main__':
    app.run(debug=True)