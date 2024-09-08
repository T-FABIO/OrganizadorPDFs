from pdf2image import convert_from_path
from PIL import Image
import pytesseract


# Configurar la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ruta al archivo PDF
pdf_1 = 'C:/Users/USUARIO/Desktop/Programacion/Python/Practica/PDFs/importacion2.pdf'


#conversion de mm a pixeles
def mmaPixeles( dpi, milimetros):
    pixeles = milimetros * (dpi/25.4) 
    return pixeles

#convierte pdf a imagen.
def paginaImg(rutaPdf, dpi, numeroPagina):

    #ruta del pdf , dpi: 600, Numeropagina : 0.
    pagina = convert_from_path(rutaPdf, dpi)
    page_image = pagina[numeroPagina]
    return page_image

page_image = paginaImg(pdf_1, 300, 0)


left = mmaPixeles(300,143.0)
top = mmaPixeles(300, 35.5)
right = mmaPixeles(300, 196.0)
bottom = mmaPixeles(300, 41.0)

# Recortar la imagen a la zona especificada
cropped_image = page_image.crop((left, top, right, bottom))

# Guardar la imagen recortada para verificarla visualmente
cropped_image.save('C:/Users/USUARIO/Desktop/Programacion/Python/Practica/img/cropped_image.png')

# Configuracion de solo numeros para una sola linea
config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

# Aplicar OCR a la imagen recortada
text = pytesseract.image_to_string(cropped_image, config=config)

# Imprimir el texto extraído en la consola
print(f"caracter extraído: '{text}'") 
