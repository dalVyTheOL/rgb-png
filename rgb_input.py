from stegano import lsb

secret = lsb.hide("input.png", "Steganography is cool")  # input.png это исходное сообщение, потом сообщение для скрытия
secret.save("output.png")  # Новый файл со скрытой информацией


