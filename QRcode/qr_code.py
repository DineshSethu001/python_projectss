import pyqrcode

url=input("Enter the URl to make QRcode:")
QR=pyqrcode.create(url)
QR.png("youtube.png",scale=1)
