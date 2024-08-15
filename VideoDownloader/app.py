
import pytube
import streamlit as st

# 1 usage

class YouTubeDownloader:

    def __init__(self, url):
        self.url= url
        self.youtube = pytube.YouTube(self.url, on_progress_callback=YouTubeDownloader.onProgress)
        self.stream = None


    def showTitle(self):
        st.write (f"**Titulo:** {self.youtube.title}")
        self.showStreams()

    def showStream(self):
        streams = self.youtube.streams
        stream_options = [
            f"Resolucion: {stream.resolution or 'N/A'} / FPS: {getattr(stream, 'fps', 'N/A')} / Tipo:{stream.mime_type}"
            for stream in streams
            
        ]

        choice = st.selectbox("Elija una opcion de stream: ", stream_options)
        self.stream in streams

    def ObtenerTamano (self):
        peso = self.stream.filesize /1000000
        return peso
    
    def


