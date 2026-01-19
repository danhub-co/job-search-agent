#!/bin/bash

echo "🚀 AI Job Search Agent - Complete Setup"
echo "======================================"

# Check Python version
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

echo "✓ Python 3 found"

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -r requirements.txt > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "✓ Dependencies installed"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

# Generate demo data
echo "🎲 Generating demo data..."
python3 generate_demo.py

# Create data directory
mkdir -p data templates

echo "✓ Project structure ready"

# Start services
echo ""
echo "🌟 Starting AI Job Search Agent..."
echo "=================================="
echo ""
echo "🔗 Frontend: http://localhost:8000"
echo "🔗 API: http://localhost:5000"
echo ""
echo "Features:"
echo "  📊 Dashboard with real-time stats"
echo "  🔍 AI-powered job search"
echo "  📝 Application tracking"
echo "  💼 LinkedIn integration"
echo "  🎯 Interview preparation"
echo "  🌙 Dark mode toggle"
echo "  📱 Mobile responsive"
echo ""

# Start Flask API in background
python3 api.py &
API_PID=$!

# Wait for API to start
sleep 2

# Start frontend server
cd frontend
python3 -m http.server 8000 &
SERVER_PID=$!

echo "✅ All services running!"
echo ""
echo "Press Ctrl+C to stop all services"

# Wait for Ctrl+C
trap "echo ''; echo '🛑 Stopping services...'; kill $API_PID $SERVER_PID 2>/dev/null; echo '✓ Services stopped'; exit" INT
wait