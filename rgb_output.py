from stegano import lsb

result = lsb.reveal("output.png")  # Файл, где предположительно находится скрытая информация
print(result)