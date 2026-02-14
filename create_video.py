import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Video parameters
output_file = "valentine-video.mp4"
width, height = 1280, 720
fps = 30
duration = 10  # 10 seconds
total_frames = fps * duration

# Video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_file, fourcc, fps, (width, height))

print("🎬 Creating Valentine Video...")
print(f"📐 Resolution: {width}x{height}")
print(f"⏱️  Duration: {duration}s ({total_frames} frames)")

def create_frame(frame_num, total_frames):
    """Create a single frame"""
    # Create image
    img = Image.new('RGB', (width, height), color=(255, 20, 147))  # Deep pink background
    draw = ImageDraw.Draw(img)
    
    # Try to use a nice font, fallback to default
    try:
        font_large = ImageFont.truetype("arial.ttf", 100)
        font_small = ImageFont.truetype("arial.ttf", 40)
    except:
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Animation progress (0.0 to 1.0)
    progress = frame_num / total_frames
    
    # Draw hearts
    heart_colors = [
        (255, 105, 180),  # Hot pink
        (255, 182, 193),  # Light pink
        (220, 20, 60),    # Crimson
        (255, 192, 203),  # Pink
    ]
    
    for i, color in enumerate(heart_colors):
        x = int(width * (0.2 + i * 0.2))
        y = int(height * (0.3 + np.sin(progress * 2 * np.pi + i) * 0.1))
        size = 80 + int(20 * np.sin(progress * 2 * np.pi + i))
        
        # Draw circle as simple heart representation
        draw.ellipse([x-size, y-size, x+size, y+size], fill=color, outline='white')
    
    # Draw main text (fade in/out)
    text_opacity = int(255 * min(progress * 2, 1, 2 - progress * 2))
    
    # Main text
    text1 = "💕 I LOVE YOU 💕"
    text2 = "Happy Valentine's Day"
    
    # Simple text rendering (PIL doesn't support opacity directly)
    # So we'll draw on separate layer
    text_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    text_draw = ImageDraw.Draw(text_img)
    
    # Text position and draw
    text1_bbox = text_draw.textbbox((0, 0), text1, font=font_large)
    text1_width = text1_bbox[2] - text1_bbox[0]
    text1_x = (width - text1_width) // 2
    text1_y = int(height * 0.4)
    
    text_draw.text((text1_x, text1_y), text1, font=font_large, fill=(255, 255, 255, text_opacity))
    
    text2_bbox = text_draw.textbbox((0, 0), text2, font=font_small)
    text2_width = text2_bbox[2] - text2_bbox[0]
    text2_x = (width - text2_width) // 2
    text2_y = int(height * 0.6)
    
    text_draw.text((text2_x, text2_y), text2, font=font_small, fill=(255, 255, 255, text_opacity))
    
    # Composite text onto main image
    img = img.convert('RGBA')
    img.paste(text_img, (0, 0), text_img)
    img = img.convert('RGB')
    
    # Add sparkles/stars
    num_stars = int(10 * progress)
    for _ in range(num_stars):
        px = np.random.randint(0, width)
        py = np.random.randint(0, height)
        size = 5
        draw.ellipse([px-size, py-size, px+size, py+size], fill=(255, 255, 255))
    
    # Convert to BGR for OpenCV
    frame_array = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    return frame_array

# Create all frames
print("\n⏳ Rendering frames...")
for i in range(total_frames):
    if (i + 1) % 30 == 0:
        print(f"  Frame {i+1}/{total_frames}")
    
    frame = create_frame(i, total_frames)
    out.write(frame)

# Release
out.release()
print(f"\n✅ Video created successfully!")
print(f"📁 File: {output_file}")
print(f"💾 Size: {os.path.getsize(output_file) / (1024*1024):.2f} MB")
print(f"\n📋 Use in valentine-ar.html:")
print(f'<source src="{output_file}" type="video/mp4">')
