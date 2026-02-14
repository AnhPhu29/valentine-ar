# 🚀 Deployment Guide - Valentine AR

Hướng dẫn chi tiết từng bước để deploy ứng dụng Valentine AR lên các platform miễn phí.

---

## 📋 Lựa Chọn Platform

| Platform | Tốc độ | Dễ sử dụng | Hỗ trợ | Giới hạn |
|----------|--------|-----------|--------|---------|
| **GitHub Pages** | 🚀 Nhanh | ⭐⭐⭐⭐⭐ | Miễn phí | Trang tĩnh |
| **Vercel** | 🚀🚀 Siêu nhanh | ⭐⭐⭐⭐ | Miễn phí | 100GB/tháng |
| **Netlify** | 🚀 Nhanh | ⭐⭐⭐⭐ | Miễn phí | 100GB/tháng |
| **Firebase Hosting** | 🚀🚀 Siêu nhanh | ⭐⭐⭐ | Miễn phí | 1GB/tháng |

**🏆 Khuyến nghị:** GitHub Pages (đơn giản) hoặc Vercel (siêu nhanh)

---

## Cách 1: GitHub Pages ⭐ (Đơn giản nhất)

### 📝 Bước 1: Tạo GitHub Account
1. Truy cập: https://github.com
2. Click "Sign up"
3. Điền email, password, username
4. Verify email
5. ✅ Tạo account xong!

### 📝 Bước 2: Tạo Repository

1. **Sau khi login GitHub:**
   - Click icon **+** góc trên phải
   - Chọn **"New repository"**

2. **Điền thông tin:**
   - Repository name: `valentine-ar` (có thể đặt tên khác)
   - Mô tả: `Valentine AR Gift - Image Tracking`
   - Chọn **"Public"** (để mọi người truy cập)
   - ✅ Tick "Add a README file"

3. **Click "Create repository"**

### 📝 Bước 3: Upload Files

1. **Trong repository vừa tạo:**
   - Click **"Add file"** → **"Upload files"**

2. **Upload các file:**
   - `valentine-ar.html` (file chính)
   - `your-image.mind` (file nhận diện ảnh - nếu có)
   - `README.md` (hướng dẫn)

3. **Click "Commit changes"** (mô tả: "Initial commit - Valentine AR")

### 📝 Bước 4: Kích Hoạt GitHub Pages

1. **Vào "Settings"** (tab trên cùng)

2. **Tìm "Pages"** ở menu bên trái

3. **Cấu hình:**
   - Branch: `main` (mặc định)
   - Folder: `/(root)` (mặc định)

4. **Click "Save"**

5. **Đợi 1-2 phút**, GitHub sẽ hiển thị URL:
   ```
   Your site is published at:
   https://USERNAME.github.io/valentine-ar/
   ```

✅ **XONG!** Bây giờ bạn có thể share link này!

---

## Cách 2: Vercel (Siêu dễ + Siêu nhanh)

### 📝 Bước 1: Chuẩn Bị

Trước tiên, bạn cần upload code lên GitHub (xem Cách 1 phần 1-3)

### 📝 Bước 2: Connect Vercel

1. **Truy cập:** https://vercel.com

2. **Click "Sign Up"**
   - Chọn **"Continue with GitHub"**
   - Authorize Vercel để truy cập GitHub

### 📝 Bước 3: Import Repository

1. **Click "New Project"**

2. **Chọn repository "valentine-ar"**

3. **Cấu hình (mặc định là OK):**
   - Framework: Other
   - Root Directory: ./
   - Environment: (để trống)

4. **Click "Deploy"**

5. **Đợi 30-60 giây**, Vercel sẽ tự động deploy

✅ **Bạn sẽ nhận được URL:**
```
https://valentine-ar.vercel.app
```

### 💡 Lợi ích Vercel:
- Mỗi khi bạn `git push` GitHub, Vercel tự động deploy
- Siêu nhanh (CDN toàn cầu)
- Không giới hạn dung lượng

---

## Cách 3: Netlify (Nếu Vercel không hoạt động)

### 📝 Bước 1: Chuẩn Bị

Giống như Vercel, upload code lên GitHub trước

### 📝 Bước 2: Connect Netlify

1. **Truy cập:** https://netlify.com

2. **Click "Sign up"**
   - Login with GitHub

### 📝 Bước 3: Deploy

1. **Click "Add new site" → "Import an existing project"**

2. **Chọn GitHub, rồi chọn repo "valentine-ar"**

3. **Cấu hình:**
   - Build command: (để trống)
   - Publish directory: ./

4. **Click "Deploy site"**

✅ **Netlify sẽ cung cấp URL:**
```
https://[random-name].netlify.app
```

---

## Cách 4: Firebase Hosting (Pro nhất)

### 📝 Bước 1: Tạo Firebase Project

1. **Truy cập:** https://firebase.google.com

2. **Login với Google Account**

3. **Click "Go to console"**

4. **Click "Create a new project"**
   - Tên project: `valentine-ar`
   - Chọn quốc gia
   - Accept terms

5. **Click "Create project"** (chờ 1-2 phút)

### 📝 Bước 2: Cài Firebase CLI

Mở **PowerShell** hoặc **Terminal**:

```bash
npm install -g firebase-tools
firebase login
```

(Nó sẽ mở browser để login Google)

### 📝 Bước 3: Initialize Firebase

```bash
cd d:\1402\
firebase init hosting
```

Trả lời các câu hỏi:
```
? What do you want to use as your public directory? .
? Configure as a single-page app? N
? Set up automatic builds? N
```

### 📝 Bước 4: Deploy

```bash
firebase deploy
```

✅ **Bạn sẽ nhận được URL:**
```
Hosting URL: https://valentine-ar.firebaseapp.com
```

---

## 🎯 So Sánh Nhanh

### GitHub Pages
```
✅ Siêu dễ
✅ Không cần setup
❌ Tốc độ trung bình
❌ Không có custom domain miễn phí
```
**Link:** `https://USERNAME.github.io/valentine-ar/`

### Vercel ⭐⭐⭐
```
✅ Siêu dễ + super nhanh
✅ Tự động deploy từ GitHub
✅ Custom domain miễn phí
✅ Environment variables
✅ Analytics
```
**Link:** `https://valentine-ar.vercel.app`

### Netlify
```
✅ Dễ
✅ Nhanh
✅ Có form builder
❌ UI phức tạp hơn Vercel
```
**Link:** `https://valentine-ar.netlify.app`

### Firebase Hosting
```
✅ Siêu nhanh
✅ Tích hợp Firebase services
✅ Custom domain
❌ Setup phức tạp
❌ CLI cần Node.js
```
**Link:** `https://valentine-ar.firebaseapp.com`

---

## 🔄 Update Code Sau Deploy

### Với GitHub Pages

```bash
# Chỉnh sửa valentine-ar.html
# Rồi:
git add .
git commit -m "Update video URL"
git push origin main

# GitHub Pages tự động update trong 1-2 phút
```

### Với Vercel

```bash
# Giống y hệt GitHub Pages
git add .
git commit -m "Update"
git push origin main

# Vercel tự động deploy trong 30 giây
```

### Với Firebase

```bash
# Chỉnh sửa file
# Rồi:
firebase deploy

# Deploy xong ngay lập tức
```

---

## 🔐 Custom Domain (Tuỳ chọn)

### Mua Domain rẻ:
- **Namecheap:** https://namecheap.com (~$0.88/năm)
- **Godaddy:** https://godaddy.com (~$1/năm)
- **Google Domains:** https://domains.google (~$7-12/năm)

### Connect Custom Domain:

**GitHub Pages:**
1. Settings → Pages → Custom domain
2. Nhập domain, click Save
3. Cập nhật DNS tại registrar

**Vercel:**
1. Project Settings → Domains
2. Nhập domain
3. Thêm DNS records (Vercel sẽ hướng dẫn)

---

## ⚠️ Troubleshooting

### Link không hoạt động
- Đợi 2-3 phút (GitHub Pages chậm)
- Check URL spelling
- Đảm bảo file HTML được upload

### Camera/Video không hoạt động
- Xem phần Troubleshooting trong README.md
- Kiểm tra URL video có truy cập được không

### 404 Not Found
- Kiểm tra link có đúng không
- Đảm bảo branch là `main` không phải `master`
- Thử hard refresh (Ctrl+Shift+R)

---

## 🎁 Cuối Cùng

**Sau khi deploy xong, bạn có một link như:**
```
https://valentine-ar.vercel.app
```

**Share link này qua:**
- 💬 Tin nhắn chỉnh
- 📱 WhatsApp
- 📧 Email
- 💌 Mạng xã hội

**Hướng dẫn người yêu:**
> Mở link này trên điện thoại (Chrome hoặc Safari)
> Bật quyền camera
> Hướng camera vào ảnh của chúng ta nhé! 💕

---

## 🆘 Still stuck?

1. Xem file [HUONG_DAN.md](HUONG_DAN.md)
2. Truy cập [Mind-AR Docs](https://docs.mindartoolkit.com/)
3. Stack Overflow: Tag `mind-ar` hoặc `a-frame`

**Chúc bạn thành công! 🎉💕**
