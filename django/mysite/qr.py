import qrcode

# Create a QR Code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Add data to the QR Code
data = "https://www.example.com"
qr.add_data(data)
qr.make(fit=True)

# Create an image object from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Save the image
img.save("example_qr_code.png")

print("QR code generated and saved as 'example_qr_code.png'")
