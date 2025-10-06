from flask import Flask, render_template, request, send_file
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    quality = request.form['quality']

    yt = YouTube(url)
    stream = yt.streams.filter(res=quality, progressive=True, file_extension='mp4').first()

    if not stream:
        return f"❌ Quality {quality} not available for this video."

    # Download file
    filename = stream.download()

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
