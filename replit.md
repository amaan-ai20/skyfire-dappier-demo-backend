# Flask OpenAI Chat API

## Overview
A REST API built with Flask that interfaces with OpenAI's Chat Completions API. The application provides endpoints for single chat messages and conversation history support.

## Project Structure
- `app.py` - Main Flask application with API endpoints
- `requirements.txt` - Python dependencies
- `README.md` - Project documentation

## Current State
✅ **RUNNING** - Flask API server running on localhost:8000

## Recent Changes
- **2025-09-03**: Initial project setup in Replit environment
- **2025-09-03**: Updated OpenAI library to version >=1.40.0 for compatibility
- **2025-09-03**: Configured backend to run on port 8000 (localhost)
- **2025-09-03**: Successfully tested all API endpoints
- **2025-09-03**: Configured for autoscale deployment

## API Endpoints
- **GET** `/health` - Health check endpoint
- **POST** `/chat` - Single message chat with OpenAI
- **POST** `/chat/conversation` - Conversation history chat with OpenAI

## Environment Setup
- **Language**: Python 3.10+ 
- **Framework**: Flask 3.0.0
- **Dependencies**: openai>=1.40.0, flask-cors==4.0.0, python-dotenv==1.0.0
- **Required Secrets**: OPENAI_API_KEY

## Architecture Notes
- Backend API runs on localhost:8000 (not port 5000 which is reserved for frontend)
- Uses latest OpenAI Python client library (v1.40+)
- CORS enabled for web application integration
- Comprehensive error handling with proper HTTP status codes
- Token usage tracking included in responses

## Deployment Configuration
- **Type**: Autoscale (suitable for stateless API)
- **Command**: python app.py
- **Status**: Configured and ready for production deployment