# Primero debemos instalar la libreria pytube.
# Para eso abrimos la terminal y escribimos pip install pytube.

from pytube import YouTube # Importamos la libreria.

url = input("Pegar url del video: ") # Creamos una variable que va contener la url del video.

yt = YouTube(url) # Recuperamos la url del input.
print(f"Descargando video... {yt.title}") # Imprimir mensaje de descarga y mostrar el nombre del video
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download() # Proceso de descarga del video con buena resolución.