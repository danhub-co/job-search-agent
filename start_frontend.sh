#!/bin/bash

echo "🚀 Starting AI Job Search Agent Frontend..."
echo ""
echo "Backend API: http://localhost:5000"
echo "Frontend UI: http://localhost:8000"
echo ""

# Install dependencies
pip install flask flask-cors > /dev/null 2>&1

# Start Flask API in background
python3 api.py &
API_PID=$!

# Start simple HTTP server for frontend
cd frontend
python3 -m http.server 8000 &
SERVER_PID=$!

echo "✓ Services started!"
echo ""
echo "Open http://localhost:8000 in your browser"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for Ctrl+C
trap "kill $API_PID $SERVER_PID; exit" INT
wait
