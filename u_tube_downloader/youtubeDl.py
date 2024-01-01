import youtube_dl

url = input("Enter the URL to download: ")

with youtube_dl.YoutubeDL() as ydl:
    try:
        info_dict = ydl.extract_info(url, download=False)
        print("Video information:", info_dict)
        ydl.download([url])
    except Exception as e:
        print("Error:", e)
