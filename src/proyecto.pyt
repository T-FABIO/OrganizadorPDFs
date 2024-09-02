from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import pytesseract

# Configurar la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#convierte pdf a imagen.
def paginaImg(rutaPdf, dpi, numeroPagina):

    #ruta del pdf , dpi: 600, Numeropagina : 0.
    pagina = convert_from_path(rutaPdf, dpi)
    page_image = pagina[numeroPagina]
    return page_image

def unir_primera_pagina(pdf1_path, pdf2_path, output_path):
    # Crear un PdfWriter para el PDF de salida
    pdf_nuevo = PdfWriter()

    # Leer el primer PDF
    pdf1_reader = PdfReader(pdf1_path)
    # Leer la primera página del primer PDF
    pagina1_pdf1 = pdf1_reader.pages[0]

    # Leer el segundo PDF
    pdf2_reader = PdfReader(pdf2_path)
    # Leer la primera página del segundo PDF
    pagina1_pdf2 = pdf2_reader.pages[0]

    # Añadir las páginas al PDF de salida
    pdf_nuevo.add_page(pagina1_pdf1)
    pdf_nuevo.add_page(pagina1_pdf2)

    # Guardar el nuevo PDF
    with open(output_path, 'wb') as output_pdf:
        pdf_nuevo.write(output_pdf)
    
paginaImgSelectividad = paginaImg(r'C:\Users\USUARIO\Desktop\Programacion\Python\Practica\PDFs\Selectividades.pdf', 600, 0)
paginaImgDeclaracion = paginaImg(r'C:\Users\USUARIO\Desktop\Programacion\Python\Practica\PDFs\DeclaracionImportacion.pdf', 600, 0)

# Recortar la imagen a la zona especificada
imagenSelectividad = paginaImgSelectividad.crop((2728, 410, 4055, 665))
imagenDeclaracion = paginaImgDeclaracion.crop((3350, 850, 4650, 1080))

# Guardar la imagen recortada para verificarla visualmente
imagenSelectividad.save(r'C:/Users/USUARIO/Desktop/Programacion/Python/Practica/img/imagenRecortadaSel.png')
imagenDeclaracion.save(r'C:/Users/USUARIO/Desktop/Programacion/Python/Practica/img/imagenRecortadaDec.png')

# Configuracion de solo numeros para una sola linea
custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

# Converimos la imagen a texto
textSelectividad = pytesseract.image_to_string(imagenDeclaracion, config=custom_config)
textDeclaracion = pytesseract.image_to_string(imagenDeclaracion, config=custom_config)

# Imprimir el texto extraído en la consola
print(f"texto extraído de la selectividad: '{textSelectividad}'") 
print(f"texto extraído de la declaracion: '{textDeclaracion}'") 

if textSelectividad == textDeclaracion:
    print("las variables son iguales")

    unir_primera_pagina(
    'C:/Users/USUARIO/Desktop/Programacion/Python/Practica/PDFs/Selectividades.pdf',
    'C:/Users/USUARIO/Desktop/Programacion/Python/Practica/PDFs/DeclaracionImportacion.pdf',
    'C:/Users/USUARIO/Desktop/Programacion/Python/Practica/PDFs/resultado.pdf')

