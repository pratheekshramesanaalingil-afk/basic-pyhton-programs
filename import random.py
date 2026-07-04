import qrcode
from PIL import Image

# Take input from user
data = input("Enter text or URL to generate QR code: bleh bleh  ")

# Create QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data to QR code
qr.add_data(data)
qr.make(fit=True)

# Create QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save image file
img.save("qrcode.png")

print("QR Code generated and saved as qrcode.png")