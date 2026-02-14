# 🔧 Hướng Dẫn Debug & Fix Lỗi

## ⚡ Nhanh: Kiểm Tra URL

### 1. Mở Developer Console (F12)
```
Windows: F12 hoặc Ctrl+Shift+I
Mac: Cmd+Option+I
```

### 2. Xem Console có lỗi nào không
- Tìm dòng có **❌** hoặc **⚠️**
- Copy lỗi đó

---

## 🎬 Video Không Phát

### Nguyên nhân 1: URL Video Sai

**Kiểm tra:**
1. Mở F12 → Console
2. Tìm dòng: `Video src: ...`
3. Copy link, mở tab mới, paste vào URL bar
4. Video phải play được trực tiếp

**Fix:**
- URL phải trỏ trực tiếp tới file video (`.mp4`, `.webm`)
- URL `https://youtube.com/...` không được (YouTube không cho phép embed trực tiếp)
- URL phải CORS-enabled

### Nguyên nhân 2: Video URL Có Lỗi CORS

**Lỗi:** `Access to XMLHttpRequest blocked by CORS policy`

**Fix - Sử dụng Proxy CORS:**
```html
<!-- Thay từ: -->
<source src="https://example.com/video.mp4" type="video/mp4">

<!-- Thành: -->
<source src="https://cors-anywhere.herokuapp.com/https://example.com/video.mp4" type="video/mp4">
```

**Hoặc upload lên Firebase Storage (đã fix CORS):**

### Nguyên nhân 3: Video Format Sai

**Kiểm tra:** File video phải là `.mp4`, `.webm`, hoặc `.ogg`

**Không hỗ trợ:** `.avi`, `.mov`, `.mkv`

**Fix:** Convert video sang MP4
- Online: https://cloudconvert.com/
- Desktop: VLC Player (File → Convert)

### Nguyên nhân 4: HTTPS Issue

**Lỗi:** Camera không hoạt động / Video không phát

**Kiểm tra:**
1. Mở F12 → Console
2. Tìm dòng: `Protocol: http:` hoặc `https:`
3. Nếu là `http://`, đó là vấn đề

**Fix:** Deploy lên HTTPS (Vercel, GitHub Pages, Firebase tất cả support HTTPS)

---

## 📸 Không Nhận Diện Ảnh

### Nguyên nhân 1: File .mind Sai

**Kiểm tra:**
1. F12 → Console  
2. Tìm dòng: `Mind-AR loaded successfully` ✅ hoặc lỗi ❌
3. Nếu có lỗi, file .mind không hoạt động

**Fix:**
1. Truy cập: https://create.mindartoolkit.com/
2. Upload ảnh kỷ niệm của bạn
3. Download file `.mind`
4. Replace URL trong HTML:
```html
mindar-image="imageTargetSrc: YOUR_NEW_.MIND_FILE_URL"
```

### Nguyên nhân 2: Ảnh Nhận Diện Sai

Ảnh phải:
- ✅ Có chi tiết rõ ràng (khuôn mặt, hoạ tiết)
- ✅ Không quá tối hoặc quá sáng
- ✅ Kích thước in: A4 hoặc lớn hơn
- ✅ Rõ nét, không mờ

Tránh:
- ❌ Ảnh trắng trơn
- ❌ Ảnh đơn sắc (một màu)
- ❌ Ảnh có quá nhiều pattern lặp lại

**Fix:** In ảnh mới có chi tiết rõ ràng, hoặc tạo lại `.mind` file

### Nguyên nhân 3: Ánh Sáng Yếu

**Problem:** Không nhận diện ảnh khi đèn tối

**Fix:**
- Sử dụng đèn tự nhiên (ánh sáng ban ngày tốt nhất)
- Tháo chế độ night mode trên camera
- Di chuyển vào nơi sáng hơn

---

## 🎮 Hình Trái Tim Không Hiện

### Nguyên nhân 1: Trình Duyệt Không Support WebGL

**Fix:**
- Dùng Chrome hoặc Firefox (hỗ trợ WebGL tốt nhất)
- Cập nhật trình duyệt lên phiên bản mới nhất

**Kiểm tra WebGL:**
1. Truy cập: https://www.khronos.org/webgl/wiki/Getting_Started/Detecting_WebGL
2. Nếu **không** có WebGL, đó là vấn đề

### Nguyên nhân 2: JavaScript Error

**Kiểm tra:**
1. F12 → Console
2. Tìm lỗi màu đỏ
3. Screenshot / copy lỗi

**Common errors:**
- `Uncaught TypeError: Cannot read property 'material'` 
  → Fix: Đợi AR load xong trước khi interact
- `Failed to load 3D model`
  → Fix: Kiểm tra file model (nếu có)

---

## 📱 Không Có Quyền Camera

### Lỗi: "Camera permission denied"

**Fix:**
1. Trên điện thoại: Settings → Apps → Browser → Camera → cho phép
2. Trên trình duyệt: Tìm icon camera trên address bar
3. Click → "Allow" hoặc "Always allow"
4. Tải lại trang (F5)

**Nếu vẫn không được:**
- Thử trình duyệt khác (Chrome, Firefox, Safari)
- Khởi động lại điện thoại
- Xóa cache trình duyệt: Settings → Clear browsing data

---

## 🌐 Lỗi Khi Deploy

### GitHub Pages - 404 Not Found

**Nguyên nhân:** File HTML không upload

**Fix:**
1. Vào GitHub repo
2. Click "Add file" → "Upload files"
3. Upload `valentine-ar.html`
4. Commit

### Vercel - Deploy Failed

**Nguyên nhân:** Repo GitHub không connected

**Fix:**
1. Chắc chắn đã push code lên GitHub: `git push origin main`
2. Vào vercel.com → "New Project" → chọn repo

### Netlify - Blank Page

**Nguyên nhân:** Build command sai

**Fix:**
1. Settings → Build & Deploy
2. Build command: (để trống)
3. Publish directory: `./` (or leave blank)
4. Deploy again

---

## 🆘 Vẫn Không Fix Được?

### Bước 1: Thu Thập Thông Tin Debug

```javascript
// Copy-paste vào F12 Console:
console.log("Browser:", navigator.userAgent);
console.log("Protocol:", window.location.protocol);
console.log("Video URL:", document.querySelector('video#memoryVideoAsset').src);
console.log("WebGL:", !!document.createElement('canvas').getContext('webgl'));
```

### Bước 2: Check Mỗi Phần

Chạy từng test này trong console:

```javascript
// Test 1: Video element
fetch('https://commondatastorage.googleapis.com/gtv-videos-library/sample/BigBuckBunny.mp4')
.then(r => console.log('✅ Video URL accessible:', r.status))
.catch(e => console.error('❌ Video URL error:', e));

// Test 2: WebGL
console.log('✅ WebGL support:', !!document.createElement('canvas').getContext('webgl'));

// Test 3: .mind file
fetch('https://cdn.jsdelivr.net/npm/mind-ar@1.2.2/examples/image-tracking/assets/band-example/band.mind')
.then(r => console.log('✅ .mind file accessible:', r.status))
.catch(e => console.error('❌ .mind file error:', e));
```

### Bước 3: Share on GitHub Issues

Nếu vẫn không fix được:
1. Tạo Issue trên GitHub: https://github.com/hiukim/mind-ar-js/issues
2. Paste output từ console
3. Mô tả vấn đề rõ ràng

---

## 📋 Checklist Debug

- [ ] ✅ F12 Console không có lỗi đỏ
- [ ] ✅ Video URL trực tiếp được (paste vào tab mới)
- [ ] ✅ Browser hỗ trợ WebGL
- [ ] ✅ Protocol là `https:` hoặc `localhost`
- [ ] ✅ Camera permission được cấp
- [ ] ✅ Ảnh nhận diện in to (A4), chi tiết rõ
- [ ] ✅ Ảnh đủ sáng (không quá tối)
- [ ] ✅ Trình duyệt cập nhật phiên bản mới

---

## 📞 Need More Help?

1. **Video không phát** → Xem "Video Không Phát"
2. **Không nhận diện ảnh** → Xem "Không Nhận Diện Ảnh"
3. **Camera không hoạt động** → Xem "Không Có Quyền Camera"
4. **Deploy lỗi** → Xem "Lỗi Khi Deploy"

**Still stuck?** Check [HUONG_DAN.md](HUONG_DAN.md) hoặc [DEPLOYMENT.md](DEPLOYMENT.md)

---

**Chúc bạn fix thành công! 💕**
