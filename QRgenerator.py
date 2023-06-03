import pyqrcode
import png
from pyqrcode import QRCode

str=input("Enter the link to create the qr")
url = pyqrcode.create(str)  
url.png('QRcode.png', scale = 8)