import qrcode

# URL for QR code
github_url = "https://github.com/Deneisha98"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(github_url)
qr.make(fit=True)

# Create the QR code image and saves it as a PNG file
img = qr.make_image(fill="black", back_color="white")
img.save("github_qr.png")
print("QR code generated and saved as github_qr.png")
