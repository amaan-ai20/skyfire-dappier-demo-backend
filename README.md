# Flask OpenAI Chat API

A simple Flask API that interfaces with OpenAI's Chat Completions API.

## Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables:**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

The API will be available at `http://localhost:5000`

## API Endpoints

### Health Check
- **GET** `/health`
- Returns the health status of the API

### Simple Chat
- **POST** `/chat`
- Send a single message to OpenAI

**Request Body:**
```json
{
  "message": "Hello, how are you?",
  "model": "gpt-3.5-turbo",
  "max_tokens": 150,
  "temperature": 0.7
}
```

**Response:**
```json
{
  "success": true,
  "response": "Hello! I'm doing well, thank you for asking. How can I help you today?",
  "model": "gpt-3.5-turbo",
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 17,
    "total_tokens": 29
  }
}
```

### Conversation Chat
- **POST** `/chat/conversation`
- Send a conversation history to OpenAI

**Request Body:**
```json
{
  "messages": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there! How can I help you?"},
    {"role": "user", "content": "What's the weather like?"}
  ],
  "model": "gpt-3.5-turbo",
  "max_tokens": 150,
  "temperature": 0.7
}
```

## Example Usage with curl

### Health Check
```bash
curl http://localhost:5000/health
```

### Simple Chat
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Tell me a joke",
    "max_tokens": 100
  }'
```

### Conversation Chat
```bash
curl -X POST http://localhost:5000/chat/conversation \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {"role": "user", "content": "Hello"},
      {"role": "assistant", "content": "Hi! How can I help you?"},
      {"role": "user", "content": "Tell me about Python"}
    ]
  }'
```

## Environment Variables

- `OPENAI_API_KEY` (required): Your OpenAI API key
- `FLASK_ENV` (optional): Flask environment (development/production)
- `FLASK_DEBUG` (optional): Enable Flask debug mode

## Error Handling

The API includes comprehensive error handling and will return appropriate HTTP status codes:

- `400 Bad Request`: Invalid request format or missing required fields
- `500 Internal Server Error`: OpenAI API errors or server issues

## Features

- ✅ Simple single-message chat endpoint
- ✅ Conversation history support
- ✅ Configurable OpenAI parameters (model, temperature, max_tokens)
- ✅ CORS enabled for web applications
- ✅ Comprehensive error handling
- ✅ Usage tracking (token counts)
- ✅ Health check endpoint