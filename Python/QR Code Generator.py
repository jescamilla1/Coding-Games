import pyqrcode

# create string to represent website
s = input("Enter url: ")
file_name = input("Enter file name with no extensions: ")

#generate QR code
qr = pyqrcode.create(s)

#create and save the png
qr.svg(file_name + ".svg", scale = 8)
print("QR code created!")
