import yt_dlp
import os
import sys

# קבלת כתובת הסרטון מהפרמטרים
if len(sys.argv) > 1:
    video_url = sys.argv[1]
else:
    print("יש לספק כתובת סרטון יוטיוב כפרמטר.")
    sys.exit(1)

cookiefile = "cookies.txt" if os.path.exists("cookies.txt") else None

# תבנית שם הקובץ: שם הסרטון + סיומת mp4
output_template = "%(title)s.%(ext)s"

ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4',
    'outtmpl': output_template,
    'merge_output_format': 'mp4'
}
if cookiefile:
    ydl_opts['cookiefile'] = cookiefile

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(video_url, download=True)
    filename = ydl.prepare_filename(info)

print(f"נשמר קובץ הווידאו בשם: {filename}")
