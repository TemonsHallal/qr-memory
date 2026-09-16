import os
import qrcode
import numpy as np

from PIL import Image, ImageDraw


# ==================================================
# GANTI INI
# ==================================================

QR_URL = "http://127.0.0.1:5000"


# ==================================================
# FOLDER OUTPUT
# ==================================================

OUTPUT_DIR = "static/qr"

os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(
    OUTPUT_DIR,
    "heart_qr.png"
)


# ==================================================
# BUAT QR
# ==================================================

qr = qrcode.QRCode(
    version=None,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=5
)

qr.add_data(QR_URL)
qr.make(fit=True)


qr_image = qr.make_image(
    fill_color="#8B1238",
    back_color="white"
).convert("RGBA")


# ==================================================
# BUAT FRAME LOVE
# ==================================================

width, height = qr_image.size

canvas_size = max(width, height) + 160

canvas = Image.new(
    "RGBA",
    (canvas_size, canvas_size),
    "white"
)

draw = ImageDraw.Draw(canvas)


# posisi QR di tengah

x = (canvas_size - width) // 2
y = (canvas_size - height) // 2


# ==================================================
# FRAME HEART
# ==================================================

frame_color = "#8B1238"

draw.rounded_rectangle(
    [
        x - 35,
        y - 35,
        x + width + 35,
        y + height + 35
    ],
    radius=45,
    outline=frame_color,
    width=10
)


# ==================================================
# TEMPEL QR
# ==================================================

canvas.alpha_composite(
    qr_image,
    (x, y)
)


# ==================================================
# TAMBAHKAN HEART DI BAGIAN BAWAH
# ==================================================

heart_x = canvas_size // 2
heart_y = y + height + 70

heart_size = 32


# lingkaran kiri

draw.ellipse(
    [
        heart_x - heart_size,
        heart_y - heart_size,
        heart_x,
        heart_y
    ],
    fill=frame_color
)


# lingkaran kanan

draw.ellipse(
    [
        heart_x,
        heart_y - heart_size,
        heart_x + heart_size,
        heart_y
    ],
    fill=frame_color
)


# segitiga bawah

draw.polygon(
    [
        (heart_x - heart_size, heart_y - 5),
        (heart_x + heart_size, heart_y - 5),
        (heart_x, heart_y + heart_size)
    ],
    fill=frame_color
)


# ==================================================
# SAVE
# ==================================================

canvas.save(
    OUTPUT_FILE,
    "PNG"
)


print()
print("======================================")
print("       ❤️ QR BERHASIL DIBUAT")
print("======================================")
print()
print("URL:")
print(QR_URL)
print()
print("File:")
print(os.path.abspath(OUTPUT_FILE))
print()