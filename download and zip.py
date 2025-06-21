# דרישות: pip install yt-dlp
import yt_dlp
import zipfile
import os

# כתובת הסרטון
video_url = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"

# שם קובץ ה-MP4 שיווצר
output_filename = "video.mp4"

# הורדת הסרטון
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': output_filename,
    'merge_output_format': 'mp4'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

# דחיסת הקובץ ל-ZIP
zip_filename = "video.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.write(output_filename)

# מחיקת קובץ ה-MP4 המקורי (אופציונלי)
os.remove(output_filename)

print(f"נוצר קובץ ZIP בשם: {zip_filename}")
