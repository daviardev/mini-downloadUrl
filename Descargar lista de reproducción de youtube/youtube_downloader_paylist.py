from pytube import Playlist # Importar libreria de playlist

url = input("Ingrese la url de la playlist que quiere descargar: ") # Ingresar url de la playlist

p = Playlist(url) # Identificar la url de playlist

print(f"Descargando lista {p.title}") # Mensaje de descarga

for i in p.videos: # Recorrer videos y hacer la conversión
    i.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download() # Descargar el video en formato mp4 con buena calidad