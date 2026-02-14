# 🎁 Valentine AR - Quick Reference

Một bản cheat sheet nhanh để không phải đọc hết tất cả.

---

## 🚀 5 Bước Nhanh Để Có Trang Web Valentine AR

### 1️⃣ Chuẩn Bị Ảnh Kỷ Niệm
```
✔️ Ảnh rõ nét, chi tiết rõ ràng (500x500px trở lên)
✔️ Không quá tối, không quá sáng
✔️ JPG hoặc PNG
```

### 2️⃣ Tạo File .mind
```
1. Truy cập: https://create.mindartoolkit.com/
2. Upload ảnh
3. Download file .mind
```

### 3️⃣ Chuẩn Bị Video/Âm Thanh (Tùy chọn)
```
- Upload video lên Firebase Storage
- Hoặc dùng video từ YouTube, Vimeo
- Copy URL lưu lại
```

### 4️⃣ Chỉnh Sửa valentine-ar.html
```html
<!-- ===== THAY ĐỔI NÀY ===== -->

<!-- 1. URL của file .mind -->
mindar-image="imageTargetSrc: YOUR_.MIND_FILE_URL"

<!-- 2. URL của video -->
<source src="YOUR_VIDEO_URL" type="video/mp4">
```

### 5️⃣ Deploy
```
GitHub Pages: Tạo repo + enable Pages (2 phút)
Vercel: Connect GitHub account + click Deploy (30s)
```

---

## 📚 URLs Quan Trọng

| Công cụ | Link |
|---------|------|
| **MindAR Creator** | https://create.mindartoolkit.com |
| **GitHub** | https://github.com |
| **Vercel** | https://vercel.com |
| **Netlify** | https://netlify.com |
| **Firebase Console** | https://console.firebase.google.com |
| **Firebase Storage** | https://firebase.google.com/docs/storage |

---

## 🔧 Chỉnh Sửa Code Nhanh

### Thay Đổi Màu Hình Trái Tim

Tìm trong HTML:
```html
<a-sphere radius="0.12" color="#ff1744" material="emissive: #ff69b4">
```

Thay:
- `#ff1744` → màu chủ
- `#ff69b4` → màu phát sáng (emissive)

Màu hex phổ biến:
- ❤️ Đỏ: `#ff1744` hoặc `#e91e63`
- 💗 Hồng: `#ff69b4` hoặc `#ff1493`
- 💛 Vàng: `#ffd700` hoặc `#ffeb3b`
- 🔮 Tím: `#9c27b0` hoặc `#e91e63`

### Thêm Audio

```html
<a-sound src="url: https://YOUR_MUSIC_URL.mp3; autoplay: true"></a-sound>
```

Thêm vào trong `<a-entity mindar-image-target="targetIndex: 0">`

### Tăng/Giảm Số Hình Trái Tim

Copy-paste khối này thêm hoặc bớt:
```html
<a-entity 
    id="heartX"
    position="-0.6 0.5 0.2"
    animation="property: position; to: -0.6 1.2 0.2; dur: 3000; loop: true"
    animation__rotation="property: rotation; to: 0 360 0; dur: 3000; loop: true">
    <a-sphere radius="0.12" color="#ff1744" material="emissive: #ff69b4">
    </a-sphere>
</a-entity>
```

---

## 🎥 Upload Video Nhanh - Firebase

### 1. Tạo Firebase Project
```
firebase.google.com → Go to Console → Create Project
```

### 2. Thêm Storage
```
Storage (menu trái) → Create Bucket
```

### 3. Upload Video
```
Click Upload → Chọn video → Copy URL
```

### Kết Quả
```
URL sẽ trông như:
https://firebasestorage.googleapis.com/v0/b/valentine-ar.appspot.com/o/video.mp4?alt=media&token=abc123
```

---

## 🐛 Fix Lỗi Phổ Biến

### ❌ Camera không hoạt động
```
→ Cho phép quyền camera
→ Dùng HTTPS trên production
→ Thử trình duyệt khác
```

### ❌ Không nhận diện ảnh
```
→ Ảnh cần chi tiết rõ ràng
→ In ảnh to (A4 size)
→ Tạo lại .mind file
→ Thử ánh sáng tự nhiên
```

### ❌ Video không phát
```
→ Kiểm tra URL có truy cập được
→ Dùng format MP4
→ Test video trên browser trước
→ Đảm bảo CORS được phép
```

### ❌ Hình trái tim không hiện
```
→ Thử trình duyệt khác
→ Cập nhật browser
→ Check console (F12) xem có error không
```

---

## 💬 Share Link

### Template Message

```
🎁 Mở link này trên điện thoại và hướng camera vào ảnh của chúng ta:

[YOUR_LINK_HERE]

Ơi anh/em, đây là surprise Valentine của em/anh 💕
Hướng camera vào ảnh kỷ niệm của chúng ta để xem hiệu ứng nhé!

✨ #ValentineAR #WebAR #TinhYeu
```

### Platform Share Tốt Nhất

- 💬 **Messenger/WhatsApp** (Link trực tiếp, đơn giản nhất)
- 📱 **Telegram** (Support tốt)
- 📧 **Email** (Formal hơn, có thể ghi thêm lời nhắn)
- 💌 **Story Facebook** (Chia sẻ công khai)

---

## 📊 Project Structure

```
valentine-ar/
│
├── valentine-ar.html          ← File chính (tất cả code ở đây)
├── your-image.mind            ← Target image (tạo từ MindAR Creator)
│
├── README.md                  ← Overview project
├── HUONG_DAN.md              ← Hướng dẫn chi tiết
├── DEPLOYMENT.md             ← Hướng dẫn deploy
├── QUICK_REFERENCE.md        ← File này
│
├── package.json              ← Node.js config
├── .gitignore                ← Git config
│
├── start-local-server.ps1    ← Script start server (Windows)
└── start-local-server.sh     ← Script start server (Mac/Linux)
```

---

## ✅ Checklist Deploy

### Trước Khi Deploy
- [ ] ✔️ Test valentine-ar.html trên local
- [ ] ✔️ Camera hoạt động được
- [ ] ✔️ Video phát được
- [ ] ✔️ Hình trái tim animate được
- [ ] ✔️ Responsive trên điện thoại

### Khi Deploy
- [ ] ✔️ Upload code lên GitHub
- [ ] ✔️ Enable GitHub Pages hoặc kết nối Vercel
- [ ] ✔️ Chờ deploy xong (1-2 phút)
- [ ] ✔️ Test link trên điện thoại
- [ ] ✔️ Share link cho người yêu!

---

## 🎪 Customization Ideas

### Thêm Chi Tiết Lãng Mạn

**Hiệu ứng Lấp Lánh:**
```html
<a-light type="point" intensity="1" position="0 0.8 0.5" 
         animation="property: intensity; to: 0.5; dur: 1000; loop: true; easing: easeInOutQuad" color="#ff69b4">
</a-light>
```

**Thêm Chữ 3D:**
```html
<a-text value="I Love You 💕" position="0 -0.8 0" 
        scale="0.5 0.5 0.5" color="#ff1744">
</a-text>
```

**Thêm Nhạc Nền:**
```html
<audio autoplay loop>
    <source src="YOUR_MUSIC_URL" type="audio/mp3">
</audio>
```

---

## 🔗 Useful Links

**Learning:**
- A-Frame Documentation: https://aframe.io/docs/
- Mind-AR Documentation: https://docs.mindartoolkit.com/
- WebAR Tutorial: https://www.youtube.com/results?search_query=webxr+ar

**Tools:**
- MindAR Creator: https://create.mindartoolkit.com/
- 3D Models: https://sketchfab.com/ (Tìm heart models)
- Color Picker: https://htmlcolorcodes.com/

**Communities:**
- A-Frame Community: https://github.com/aframevr/aframe
- Mind-AR Issues: https://github.com/hiukim/mind-ar-js/issues

---

## ❓ FAQ

**Q: Ảnh kỷ niệm cần to bao nhiêu?**
A: Tối thiểu A5 (14x21cm), tốt nhất A4 (21x29.7cm)

**Q: Video cần bao lâu?**
A: 30 giây - 2 phút là tốt. Quá dài sẽ tốn bandwidth.

**Q: Có giới hạn file size không?**
A: Firebase free: 1GB/tháng. Vercel: 100GB/tháng. Đủ rồi!

**Q: Có hoạt động offline không?**
A: Không. Cần internet để tải library và video.

**Q: Bao nhiêu người có thể access cùng lúc?**
A: Không giới hạn. Các platform đều auto-scale.

**Q: Di chuyển camera như thế nào?**
A: Từ từ hướng camera vào ảnh, di chuyển trong phạm vi ảnh. Không cần di chuyển nhanh.

---

## 🎉 Bạn sẵn sàng rồi!

```
1. Tạo .mind file
2. Chỉnh sửa valentine-ar.html
3. Upload lên GitHub
4. Deploy với Vercel
5. Share link
6. Xem người yêu bất ngờ 💕
```

**Chúc bạn có một Valentine tuyệt vời! 🌹✨**

---

*Cần help? Xem file HUONG_DAN.md hoặc DEPLOYMENT.md*
