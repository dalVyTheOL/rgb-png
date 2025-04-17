from stegano import lsb

secret = lsb.hide("input.png", "Steganography is cool")  # input.png это исходное изображение, потом сообщение для скрытия
secret.save("output.png")  # Новый файл со скрытой информацией


