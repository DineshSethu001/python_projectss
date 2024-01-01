import webbrowser as wb
import os

def workauto():
    text_editor="C:\\Program Files\\Sublime Text\\sublime_text.exe"
    os.startfile(text_editor)
    chrome_path="C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    # url=input("enter the url")
    urls=("adultEmpire.com",
          "youtube.com",
          'https://www.google.com/search?q=masstamilan&rlz=1C1VDKB_enIN1080IN1081&oq=masstam&gs_lcrp=EgZjaHJvbWUqDQgAEAAYgwEYsQMYgAQyDQgAEAAYgwEYsQMYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDINCAQQABiDARixAxiABDIHCAUQABiABDIHCAYQABiABDIGCAcQBRhAqAIAsAIA&sourceid=chrome&ie=UTF-8')

    for url in urls:
        wb.get(chrome_path).open(url)

workauto()