###ENCODING -- MAKE THE QRCODE AND ADD INFORMATION TO IT 
# import qrcode

# data = "https://bit.ly/DimakatsoSema" #the information we want to include 

# qr = qrcode.QRCode(version = 1, box_size=10, border =5)

# qr.add_data(data)

# qr.make(fit=True)

# img = qr.make_image(fill_color = "pink", back_color = "white")

# # img = qrcode.make(data)
# img.save("c:/Users/dsema/OneDrive/Drive Documents/Personal documents/Backend developer/PYTHON/Beginner Projects/myqrcode2.png")

###DECODING -- EXTRACTING INFORMATION FROM THE QRCODE 
from pyzbar.pyzbar import decode
from PIL import Image 

img = Image.open("c:/Users/dsema/OneDrive/Drive Documents/Personal documents/Backend developer/PYTHON/Beginner Projects/myqrcode.png")

result = decode(img)

print(result)