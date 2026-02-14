# 💕 Valentine AR - Web Augmented Reality Gift

## ✨ Tính Năng

✅ **Image Tracking AR** - Nhận diện ảnh thực tế qua camera  
✅ **Video Kỷ Niệm** - Phát video đè lên ảnh kỷ niệm  
✅ **Hiệu Ứng 3D** - Trái tim bay lơ lửng xung quanh  
✅ **Responsive Design** - Tương thích mọi thiết bị  
✅ **Easy Deploy** - Deploy chỉ trong 2 phút  
✅ **Console Logging** - Dễ debug lỗi  

---

## 🚀 Quick Start

### 1. Clone hoặc Download file

```bash
git clone https://github.com/USERNAME/valentine-ar.git
cd valentine-ar
```

### 2. Test URL & Setup nhanh

**Bước này rất quan trọng!** Mở file [test-url.html](test-url.html) trong trình duyệt để:
- ✅ Kiểm tra WebGL support
- ✅ Test video URL có hoạt động
- ✅ Test .mind file có load được
- ✅ Kiểm tra CORS issues

### 3. Tạo file .mind của bạn

Truy cập: **https://create.mindartoolkit.com/**
- Upload ảnh kỷ niệm của bạn
- Download file `.mind`
- Đặt vào folder project

### 4. Sửa file `valentine-ar.html`

Tìm và thay:
- **Line 185:** Thay `imageTargetSrc` thành đường dẫn `.mind` file của bạn
- **Line 161:** Thay URL video (lấy từ Firebase, YouTube, v.v.)

### 5. Deploy

#### GitHub Pages (Miễn phí):
```bash
git add .
git commit -m "Valentine AR"
git push origin main
# Bật Settings > Pages > Deploy from branch: main
```

#### Vercel (Siêu dễ):
```
Truy cập vercel.com → Import repo → Deploy
```

---

## 📚 File Structure

```
valentine-ar/
├── valentine-ar.html      # Main AR application ⭐
├── test-url.html          # URL Test Tool 🧪 (kiểm tra trước)
├── your-image.mind        # Target image file
│
├── README.md              # File này
├── QUICK_REFERENCE.md     # Cheat sheet 5 phút ⚡
├── HUONG_DAN.md          # Hướng dẫn chi tiết 📖
├── DEPLOYMENT.md         # Hướng dẫn deploy 🚀
├── TROUBLESHOOTING.md    # Fix lỗi 🔧
│
├── package.json
├── .gitignore
└── start-local-server.*  # Start server scripts
```

---

## 🧪 Test Trước Khi Deploy

**LẤY QUAN TRỌNG:** Mở [test-url.html](test-url.html) để:
1. ✅ Kiểm tra browser support
2. ✅ Test video URL có stream được
3. ✅ Test .mind file file có download được
4. ✅ Phát hiện CORS issues

```bash
# Mở trong trình duyệt:
file:///d:/1402/test-url.html
```

---

## 🎨 Tùy Chỉnh

### Thay Đổi Màu Hình Trái Tim
Trong `<style>`, tìm `#ff1744` (màu đỏ) và `#ff69b4` (hồng), thay bằng màu hex của bạn.

### Thêm Âm Thanh
Thêm vào phần `<a-entity>` target:
```html
<a-sound src="url: URL_NHAC; autoplay: true"></a-sound>
```

### Tăng/Giảm Số Hình Trái Tim
Copy-paste các `<a-entity id="heart*">` blocks thêm hoặc bớt.

### Thay Đổi Kích Thước Video
Sửa `width="1.6" height="0.9"` thành giá trị tùy ý:
- Tỷ lệ 16:9 → `width="1.6" height="0.9"`
- Tỷ lệ 4:3 → `width="1.2" height="0.9"`

---

## 🌐 Deploy Urls

Sau khi deploy, bạn sẽ có link như:
- **GitHub Pages:** `https://USERNAME.github.io/valentine-ar/`
- **Vercel:** `https://valentine-ar.vercel.app/`

**Share link này qua:**
- 💬 Tin nhắn
- 📱 WhatsApp
- 📧 Email
- 💌 Mạng xã hội

---

## 📖 Tài Liệu Chi Tiết

| Tài Liệu | Nội Dung | Time |
|---------|---------|------|
| [QUICK_REFERENCE.md](QUICK_REFERENCE.md) | Cheat sheet 5 phút | ⚡ 5 min |
| [HUONG_DAN.md](HUONG_DAN.md) | Hướng dẫn full | 📖 30 min |
| [DEPLOYMENT.md](DEPLOYMENT.md) | Cách deploy (4 platform) | 🚀 10 min |
| [TROUBLESHOOTING.md](TROUBLESHOOTING.md) | Fix lỗi & debug | 🔧 15 min |

---

## 🛠️ Tech Stack

- **A-Frame:** WebGL 3D framework (aframe.io)
- **Mind-AR.js:** Image tracking AR library
- **Three.js:** 3D rendering (qua A-Frame)
- **HTML5 Video:** Embedded video playback

---

## 🎯 Browser Support

| Browser | Windows | Mac | iOS | Android |
|---------|---------|-----|-----|---------|
| Chrome  | ✅      | ✅  | ✅  | ✅      |
| Firefox | ✅      | ✅  | ✅  | ✅      |
| Safari  | ✅      | ✅  | ✅  | ⚠️      |
| Edge    | ✅      | ⚠️  | ⚠️  | ✅      |

✅ = Full support  
⚠️ = Partial support  
❌ = Not supported

---

## 💡 Tips

1. **Camera Quality:** Đảm bảo camera điện thoại hoạt động tốt
2. **Lighting:** Ánh sáng ngoài trời tốt hơn ánh sáng trong nhà
3. **Image Size:** In ảnh quá nhỏ khó nhận diện, in A4 size là tốt
4. **Smooth Motion:** Di chuyển camera từ từ để AR hoạt động mượt
5. **Phone Angle:** Nghiêng điện thoại để thấy toàn bộ ảnh
6. **Test trước:** Sử dụng [test-url.html](test-url.html) để phát hiện lỗi sớm

---

## 🔍 Debug & Troubleshooting

### Video Không Phát?
1. Mở file [test-url.html](test-url.html)
2. Test Video URL - nếu fail, URL sai
3. Xem [TROUBLESHOOTING.md](TROUBLESHOOTING.md) phần "Video Không Phát"

### Không Nhận Diện Ảnh?
1. Kiểm tra ảnh có chi tiết rõ không (không trắng trơn)
2. Tạo lại .mind file trên https://create.mindartoolkit.com/
3. Xem [TROUBLESHOOTING.md](TROUBLESHOOTING.md) phần "Không Nhận Diện Ảnh"

### Lỗi Camera?
1. Cấp quyền camera cho trình duyệt
2. Thử HTTPS nếu test trên công cộng
3. Xem [TROUBLESHOOTING.md](TROUBLESHOOTING.md) phần "Không Có Quyền Camera"

**Vẫn không fix?** → Xem [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## ⚠️ Lưu Ý Quan Trọng

### HTTPS Requirement
- Một số trình duyệt yêu cầu **HTTPS** để truy cập camera
- Local testing: `localhost` được phép (không cần HTTPS)
- Production: Deploy lên GitHub Pages, Vercel, Firebase (tất cả hỗ trợ HTTPS)

### CORS Issues
- Video URL phải từ server có CORS enabled
- Khuyến nghị: Firebase Storage, YouTube CDN, hoặc GitHub Raw
- Tránh: URL từ server cá nhân không cấu hình CORS

### Video Format
- Hỗ trợ: `.mp4`, `.webm`, `.ogg`
- Không hỗ trợ: `.avi`, `.mov`, `.mkv`
- Default: MP4 là tốt nhất (hỗ trợ trên mọi device)

---

## 📝 License

**Free to use for personal & commercial projects**

---

## 💕 Made with Love for Valentine's Day

**Chúc bạn có một Valentine thật ngọt ngào! 🎁✨**

---

### 🆘 Cần Help?

1. **Nhanh**: Xem [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
2. **Chi tiết**: Xem [HUONG_DAN.md](HUONG_DAN.md)
3. **Deploy**: Xem [DEPLOYMENT.md](DEPLOYMENT.md)
4. **Fix lỗi**: Xem [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
5. **Test URL**: Mở [test-url.html](test-url.html)
6. **Liên hệ**: GitHub Issues hoặc check [Mind-AR Docs](https://docs.mindartoolkit.com/)

---

*Last updated: February 14, 2026*
