import yt_dlp
import os

url = input("Digite o link da playlist: ")
output_folder = input("Digite o caminho da pasta onde os vídeos serão salvos: ")


if not os.path.exists(output_folder):
    os.makedirs(output_folder)
ydl_opts = {
    'format': 'bestvideo[height<=1080]+bestaudio/best',  
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'), 
    'merge_output_format': 'mp4',  
    'postprocessors': [{
        'key': 'FFmpegVideoConvertor',  
        'preferedformat': 'mp4',
    }],
    'noplaylist': False,  
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("\n🎉 Download da playlist concluído!")
