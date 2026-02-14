# Valentine AR - Local Server Setup (Windows PowerShell)

Write-Host "================================" -ForegroundColor Magenta
Write-Host "  Valentine AR - Local Server Setup" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Magenta
Write-Host ""

# Check if Node.js is installed
$nodeVersion = node -v 2>$null
if ($null -eq $nodeVersion) {
    Write-Host "❌ Node.js không được tìm thấy!" -ForegroundColor Red
    Write-Host "📥 Cài đặt từ: https://nodejs.org/" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Node.js version: $nodeVersion" -ForegroundColor Green

# Install http-server globally if not already installed
Write-Host ""
Write-Host "⏳ Kiểm tra http-server..." -ForegroundColor Yellow

$httpServer = npm list -g http-server 2>$null | Select-String "http-server"
if ($null -eq $httpServer) {
    Write-Host "📥 Cài đặt http-server toàn cục..." -ForegroundColor Yellow
    npm install -g http-server
}

Write-Host "✅ http-server sẵn sàng" -ForegroundColor Green

# Start local server
Write-Host ""
Write-Host "🚀 Khởi động local server..." -ForegroundColor Cyan
Write-Host ""
Write-Host "📱 Mở URL này trên điện thoại:" -ForegroundColor Yellow
Write-Host "   http://<YOUR_PC_IP>:8080/valentine-ar.html" -ForegroundColor Cyan
Write-Host ""
Write-Host "💡 Để tìm IP của PC:" -ForegroundColor Yellow
Write-Host "   ipconfig | Select-String 'IPv4 Address'" -ForegroundColor White
Write-Host ""
Write-Host "❌ Nhấn Ctrl+C để dừng server" -ForegroundColor Red
Write-Host ""

http-server -c-1
