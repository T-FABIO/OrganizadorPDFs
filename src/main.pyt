from pdf2image import convert_from_path
from PIL import Image
import pytesseract


# Configurar la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta al archivo PDF
pdf_path = 'C:/Users/USUARIO/Desktop/Programacion/Python/Practica/PDFs/7.pdf'

# Convertir la primera página del PDF a una imagen
pages = convert_from_path(pdf_path, 600)  # 600 es la resolución en DPI

# Seleccionar la primera página (índice 0)
page_image = pages[0]

# Definir la zona específica de la página (x, y, ancho, alto)
#left = 730, top = 100, width = 200, height = 45
left = 3350
top = 900
width = 1300
height = 174

# Recortar la imagen a la zona especificada
cropped_image = page_image.crop((left, top, left + width, top + height))

# Guardar la imagen recortada para verificarla visualmente
cropped_image.save('C:/Users/USUARIO/Desktop/Programacion/Python/Practica/img/cropped_image.png')

# Configuración de Tesseract para OCR de un solo carácter
config = '--psm 10 -c tessedit_char_whitelist=0123456789'

# Aplicar OCR a la imagen recortada
text = pytesseract.image_to_string(cropped_image, config=config)

# Imprimir el texto extraído en la consola
print(f"caracter extraído: '{text}'") 