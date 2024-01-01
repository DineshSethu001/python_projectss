import pyshorteners

url=input("Enter the url to strink:-")

print(pyshorteners.Shortener().tinyurl.short(url))