# 💕 Hướng Dẫn Tạo Trang Web Quà Valentine AR

## 📋 Mục lục
1. [Tùy chỉnh ảnh kỷ niệm](#1-tùy-chỉnh-ảnh-kỷ-niệm)
2. [Tạo file .mind](#2-tạo-file-mind)
3. [Thay đổi video và âm thanh](#3-thay-đổi-video-và-âm-thanh)
4. [Deploy lên GitHub Pages](#4-deploy-lên-github-pages)
5. [Deploy lên Vercel](#5-deploy-lên-vercel)
6. [Troubleshooting](#6-troubleshooting)

---

## 1. Tùy chỉnh ảnh kỷ niệm

### Yêu cầu ảnh tốt:
- **Độ phân giải:** Tối thiểu 500x500px, tốt nhất 1000x1000px
- **Chi tiết:** Ảnh cần có nhiều điểm đặc trưng (họa tiết, khuôn mặt, vật thể rõ ràng)
- **Độ sáng:** Không quá tối hoặc quá sáng
- **Định dạng:** JPG hoặc PNG

❌ **Tránh:**
- Ảnh trắng trơn hoặc quá đơn giản
- Ảnh mờ hoặc bị chuyển động
- Ảnh có quá nhiều phần giống nhau lặp lại

✅ **Gợi ý cho Valentine:**
- Ảnh cặp đôi
- Ảnh kỷ niệm chung
- Ảnh chân dung rõ nét

---

## 2. Tạo file `.mind` từ ảnh

### Cách 1: Sử dụng MindAR Web Tool (Dễ nhất) ⭐

1. Truy cập: https://create.mindartoolkit.com/
2. Click **"Create New"**
3. Upload ảnh kỷ niệm của bạn
4. Hệ thống sẽ tự động tạo file `.mind`
5. Download file `.mind` về máy tính

### Cách 2: Sử dụng Command Line (Dành cho dev)

```bash
# Cài đặt MindAR CLI
npm install -g mindar@latest

# Tạo file .mind từ ảnh
mindar create-target <đường-dẫn-ảnh.jpg>
```

### Cách 3: Sử dụng Docker (Tùy chọn)

```bash
docker run -it -v $(pwd):/workspace mindar mindar create-target /workspace/image.jpg
```

---

## 3. Thay đổi Video và Âm Thanh

### Cách 1: Upload video lên URL công cộng

Bạn có thể sử dụng:
- **YouTube:** Lấy link embed video
- **Vimeo:** https://vimeo.com/video_id
- **GitHub:** Commit video vào repo và lấy raw link
- **Imgur:** Upload video up và lấy link
- **Firebase Storage:** (Hướng dẫn bên dưới)

### Cách 2: Upload Video lên Firebase Storage (Miễn phí, dung lượng tốt)

#### Bước 1: Tạo Firebase Project
```
1. Truy cập https://firebase.google.com
2. Login với Google Account
3. Click "Go to console"
4. Click "Create a new project"
5. Điền tên project (vd: "valentine-ar")
6. Chọn quốc gia
```

#### Bước 2: Cấu hình Storage
```
1. Vào "Storage" trong menu bên trái
2. Click "Create bucket"
3. Chọn vị trí (gần bạn nhất tốt)
4. Chọn "Start in test mode" (Cho test)
5. Hoàn thành
```

#### Bước 3: Upload Video
```
1. Click "Upload file"
2. Chọn video kỷ niệm của bạn
3. Đợi upload hoàn thành
4. Click vào file video
5. Copy link trong "URL"
```

### Cách 3: Chỉnh sửa HTML để thay URL

Mở file `valentine-ar.html` tìm dòng:

```html
<!-- Thay URL này thành video của bạn -->
<source src="https://www.w3schools.com/html/mov_bbb.mp4" type="video/mp4">
```

Thành:
```html
<source src="YOUR_VIDEO_URL_HERE" type="video/mp4">
```

---

## 4. Deploy lên GitHub Pages (Siêu đơn giản)

### Bước 1: Tạo GitHub Account
- Truy cập: https://github.com
- Đăng ký hoặc đăng nhập

### Bước 2: Tạo Repository mới
```
1. Click "+" góc trên phải → "New repository"
2. Đặt tên: valentine-ar (hoặc tên tuỳ thích)
3. Chọn "Public"
4. ✅ Tick "Add a README file"
5. Click "Create repository"
```

### Bước 3: Upload file
```
1. Trong repo, click "Add file" → "Upload files"
2. Kéo file valentine-ar.html vào
3. Kéo file .mind vào (nếu không dùng URL tập trung)
4. Scroll xuống, enter commit message: "Initial commit"
5. Click "Commit changes"
```

### Bước 4: Kích hoạt GitHub Pages
```
1. Click "Settings"
2. Scroll tìm "Pages"
3. Chọn "Deploy from a branch"
4. Branch: "main", Folder: "(root)"
5. Click "Save"
6. Đợi 1-2 phút, trang sẽ hiển thị URL: 
   https://USERNAME.github.io/valentine-ar/
```

✅ **Xong! Link của bạn đã sẵn sàng!**

---

## 5. Deploy lên Vercel (Còn dễ hơn)

### Bước 1: Connect GitHub
```
1. Truy cập: https://vercel.com
2. Click "Sign Up"
3. Chọn "Continue with GitHub"
4. Authorize Vercel
```

### Bước 2: Import Project
```
1. Click "New Project"
2. Chọn repo "valentine-ar"
3. Không cần cấu hình gì
4. Click "Deploy"
5. Đợi ~30 giây
```

✅ **Vercel sẽ tự động cấp URL:** `https://valentine-ar.vercel.app`

**Mỗi lần bạn update code trên GitHub, Vercel tự động deploy!**

---

## 6. Cập nhật ảnh nhận diện (Target Image)

### Hiện tại, code đang sử dụng:
```
imageTargetSrc: https://cdn.jsdelivr.net/npm/mind-ar@1.2.2/examples/image-tracking/assets/band-example/band.mind
```

### Để thay đổi:

#### Cách 1: Host file .mind trên GitHub
```
1. Upload file .mind lên GitHub repo
2. Lấy Raw link: 
   https://raw.githubusercontent.com/USERNAME/valentine-ar/main/your-image.mind
3. Thay vào code:
   imageTargetSrc: "https://raw.githubusercontent.com/USERNAME/valentine-ar/main/your-image.mind"
```

#### Cách 2: Host trên Firebase Storage
```
1. Upload .mind file vào Firebase Storage
2. Copy URL và thay vào code
```

### Sửa file HTML:
```html
<!-- Tìm dòng này: -->
mindar-image="imageTargetSrc: https://cdn.jsdelivr.net/npm/mind-ar@1.2.2/examples/image-tracking/assets/band-example/band.mind; maxTrack: 10; warmupCount: 8"

<!-- Thay thành: -->
mindar-image="imageTargetSrc: YOUR_MIND_FILE_URL; maxTrack: 10; warmupCount: 8"
```

---

## 7. Troubleshooting

### ❌ Camera không hoạt động
- **Nguyên nhân:** Chưa cấp quyền camera
- **Giải pháp:** 
  1. Để ý icon camera trên trình duyệt
  2. Click và chọn "Allow" cho quyền camera
  3. Tải lại trang (F5)

### ❌ Không nhận diện ảnh
- **Nguyên nhân:** Ảnh không có đủ chi tiết hoặc file .mind sai
- **Giải pháp:**
  1. Kiểm tra ảnh có rõ nét không
  2. Thử in ảnh to ra, hướng camera vào
  3. Tạo lại file .mind trên https://create.mindartoolkit.com

### ❌ Video không phát
- **Nguyên nhân:** URL video sai hoặc CORS issue
- **Giải pháp:**
  1. Kiểm tra URL có valid không
  2. Dùng video từ Firebase Storage hoặc YouTube
  3. Video phải là định dạng .mp4

### ❌ Lỗi CORS
- **Nguyên nhân:** Server không cho phép lấy tài nguyên
- **Giải pháp:**
  1. Dùng Firebase Storage (đã cấu hình CORS)
  2. Dùng CDN công cộng (jsdelivr, cloudinary)

### ❌ Hình trái tim không hiển thị
- **Nguyên nhân:** Trình duyệt không support WebGL
- **Giải pháp:**
  1. Dùng trình duyệt có hỗ trợ WebGL (Chrome, Firefox, Safari)
  2. Cập nhật trình duyệt phiên bản mới nhất

---

## 🎁 Tips Thêm

### Tùy chỉnh Giao Diện
- **Màu vàng (love pink):** Tìm `#ff1744` trong CSS, thay màu hex khác
- **Véc-tơ hình trái tim:** Có nhiều model 3D free trên sketchfab.com

### Tăng Hiệu Ứng
Thêm âm thanh nền (nhạc Valentine):
```html
<audio id="bgMusic" autoplay loop muted>
    <source src="YOUR_MUSIC_URL" type="audio/mp3">
</audio>
```

Bỏ `muted` sau khi người dùng click Play.

### Share trên Mạng Xã Hội
```
🎁 Mở link này với điện thoại và hướng camera vào ảnh của dúng ta:
[YOUR_LINK_HERE]

Ơi anh/em, đây là surprise Valentine của em/anh 💕
```

---

## Chúc bạn thành công! 💕✨

Nếu có vấn đề, comment GitHub Issues hoặc liên hệ support.
