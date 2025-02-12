import yt_dlp
import os

url = input("Digite o link do vídeo: ")
output_folder = input("Digite o caminho da pasta onde o vídeo será salvo: ")

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

ydl_opts = {
    'format': 'bv*[height<=1080]+ba/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'merge_output_format': 'mp4',
    'postprocessors': [{
        'key': 'FFmpegMerger',
    }],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("\n🎉 Download do vídeo concluído!")
