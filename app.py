import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable is required")

client = OpenAI(api_key=openai_api_key)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "Flask OpenAI API is running"})

@app.route('/chat', methods=['POST'])
def chat_completion():
    """
    Chat completion endpoint that forwards requests to OpenAI
    
    Expected JSON payload:
    {
        "message": "Your message here",
        "model": "gpt-3.5-turbo" (optional, defaults to gpt-3.5-turbo),
        "max_tokens": 150 (optional, defaults to 150),
        "temperature": 0.7 (optional, defaults to 0.7)
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Extract message from request
        user_message = data.get('message')
        if not user_message:
            return jsonify({"error": "Message is required"}), 400
        
        # Extract optional parameters with defaults
        model = data.get('model', 'gpt-3.5-turbo')
        max_tokens = data.get('max_tokens', 150)
        temperature = data.get('temperature', 0.7)
        
        # Create chat completion request
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "user", "content": user_message}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        # Extract the response content
        assistant_message = response.choices[0].message.content
        
        # Return the response
        return jsonify({
            "success": True,
            "response": assistant_message,
            "model": model,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/chat/conversation', methods=['POST'])
def chat_conversation():
    """
    Chat completion endpoint that supports conversation history
    
    Expected JSON payload:
    {
        "messages": [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"},
            {"role": "user", "content": "How are you?"}
        ],
        "model": "gpt-3.5-turbo" (optional),
        "max_tokens": 150 (optional),
        "temperature": 0.7 (optional)
    }
    """
    try:
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        
        # Extract messages from request
        messages = data.get('messages')
        if not messages or not isinstance(messages, list):
            return jsonify({"error": "Messages array is required"}), 400
        
        # Validate message format
        for msg in messages:
            if not isinstance(msg, dict) or 'role' not in msg or 'content' not in msg:
                return jsonify({"error": "Each message must have 'role' and 'content' fields"}), 400
        
        # Extract optional parameters with defaults
        model = data.get('model', 'gpt-3.5-turbo')
        max_tokens = data.get('max_tokens', 150)
        temperature = data.get('temperature', 0.7)
        
        # Create chat completion request
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature
        )
        
        # Extract the response content
        assistant_message = response.choices[0].message.content
        
        # Return the response
        return jsonify({
            "success": True,
            "response": assistant_message,
            "model": model,
            "usage": {
                "prompt_tokens": response.usage.prompt_tokens,
                "completion_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            }
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)