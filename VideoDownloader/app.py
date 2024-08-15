
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

