from PIL import Image, ImageDraw, ImageFont
import random

# Create target image for AR
width, height = 800, 600
img = Image.new('RGB', (width, height), color='white')
draw = ImageDraw.Draw(img)

# Draw colorful background
for i in range(0, width, 50):
    for j in range(0, height, 50):
        color = (random.randint(200, 255), random.randint(150, 255), random.randint(200, 255))
        draw.rectangle([i, j, i+45, j+45], fill=color)

# Draw large heart
draw.ellipse([200, 150, 350, 300], fill='#ff1744')
draw.ellipse([350, 150, 500, 300], fill='#ff1744')
draw.polygon([(200, 250), (425, 450), (500, 250)], fill='#ff1744')

# Draw text
try:
    font = ImageFont.truetype("arial.ttf", 80)
except:
    font = ImageFont.load_default()

# Add distinctive features for AR tracking
draw.text((250, 500), "LOVE", fill='#ff1744', font=font)
draw.rectangle([50, 50, 750, 550], outline='#ff1744', width=10)

# Add patterns for better AR tracking
for x in range(100, 700, 100):
    draw.ellipse([x, 100, x+50, 150], fill='#e91e63')

# Save
output_path = "d:/1402/target-image.jpg"
img.save(output_path, quality=95)
print(f"✅ Ảnh target đã tạo: {output_path}")
print(f"📏 Size: {width}x{height}")
print(f"📝 In ảnh này ra hoặc hiển thị trên màn hình để test AR!")
