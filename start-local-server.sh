#!/bin/bash

# Valentine AR - Local Server Setup (macOS/Linux)

echo "================================"
echo "  Valentine AR - Local Server Setup"
echo "================================"
echo ""

# Check if Node.js is installed
if ! command -v node &> /dev/null
then
    echo "❌ Node.js not found!"
    echo "📥 Install from: https://nodejs.org/"
    exit 1
fi

NODE_VERSION=$(node -v)
echo "✅ Node.js version: $NODE_VERSION"

# Install http-server if not already installed
echo ""
echo "⏳ Checking http-server..."

if ! npm list -g http-server &> /dev/null
then
    echo "📥 Installing http-server globally..."
    npm install -g http-server
fi

echo "✅ http-server is ready"

# Start local server
echo ""
echo "🚀 Starting local server..."
echo ""

# Get local IP
LOCAL_IP=$(ipconfig getifaddr en0 || hostname -I | awk '{print $1}')

echo "📱 Open this URL on your phone:"
echo "   http://$LOCAL_IP:8080/valentine-ar.html"
echo ""
echo "💡 If above doesn't work, use your PC IP from:"
echo "   ifconfig | grep 'inet '"
echo ""
echo "❌ Press Ctrl+C to stop server"
echo ""

http-server -c-1 -p 8080
