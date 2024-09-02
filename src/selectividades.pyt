from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import pytesseract

# Configurar la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ruta_pdf_selectividades = r'C:\Users\USUARIO\Desktop\Programacion\Python\Practica\PDFs\selectividad.pdf'
ruta_pdf_importacion = r'C:\Users\USUARIO\Desktop\Programacion\Python\Practica\PDFs\importacion.pdf'
ruta_pdf_nuevo = r'C:\Users\USUARIO\Desktop\Programacion\Python\Practica\PDFs\pdfNuevo1.pdf'
# lista de numeros de formularios
numeros_de_selectividades = []
numeros_de_importacion = []

def obtener_total_paginas(ruta_pdf):
    # Crear un objeto PdfReader para leer el PDF
    lector_pdf = PdfReader(ruta_pdf)
    
    # Obtener el número total de páginas
    total_paginas = len(lector_pdf.pages)
    
    return total_paginas

def organizar_pdfs(pdf1_path, pdf2_path, arreglo1, arreglo2, output_path):
    # Cargar los PDFs
    pdf1 = PdfReader(pdf1_path)
    pdf2 = PdfReader(pdf2_path)
    writer = PdfWriter()

    i_pdf2 = 0  # Índice para recorrer arreglo2

    for i_pdf1, page_num in enumerate(arreglo1):
        # Añadir la página del PDF1 correspondiente
        writer.add_page(pdf1.pages[i_pdf1])

        # Añadir las páginas del PDF2 que coinciden o son "respaldo"
        while i_pdf2 < len(arreglo2):
            if arreglo2[i_pdf2] == page_num:
                # Añadir la página del PDF2 que coincide
                writer.add_page(pdf2.pages[i_pdf2])
                i_pdf2 += 1
                # Añadir respaldos si los hay
                while i_pdf2 < len(arreglo2) and arreglo2[i_pdf2] == "respaldo":
                    writer.add_page(pdf2.pages[i_pdf2])
                    i_pdf2 += 1
                break
            i_pdf2 += 1

    # Guardar el PDF de salida
    with open(output_path, "wb") as output_pdf:
        writer.write(output_pdf)


# Obtenemos el total de las paginas de los pdfs
total_paginas_selectividades = obtener_total_paginas(ruta_pdf_selectividades)
total_paginas_importaciones = obtener_total_paginas(ruta_pdf_importacion)


# Convierte los pdfs a imagenes
imagenPdfSelectividad = convert_from_path(ruta_pdf_selectividades, 600)
imagenpdfImportacion = convert_from_path(ruta_pdf_importacion, 600)

# Obtenemos los numeros de formularios del pdf de selectividaes

for i in range(total_paginas_selectividades):
    
    PaginaImagenSelectividad = imagenPdfSelectividad[i]

    # Recorta el cuadro especifico en la imagen
    cuadroImagenSelectividad = PaginaImagenSelectividad.crop((2728, 410, 4055, 665))

    # Configuracion de solo numeros para una sola linea
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

    # Converimos la imagen a texto
    textSelectividad = pytesseract.image_to_string(cuadroImagenSelectividad, config=custom_config)

    if textSelectividad == '':
        
        cuadroImagenSelectividad = PaginaImagenSelectividad.crop((2980, 200, 4150, 420))
        
        # Configuracion de solo numeros para una sola linea
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

        # Converimos la imagen a texto
        textSelectividad = pytesseract.image_to_string(cuadroImagenSelectividad, config=custom_config)
        numeros_de_selectividades.append(textSelectividad)
    else:
        # Guardar los numeros de formularios en una lista
        numeros_de_selectividades.append(textSelectividad)


for i, numero_selectividad in enumerate(numeros_de_selectividades):
    print(f"i: {i}, numeros: {numero_selectividad}")

#obtenemos los numeros de formularios de las declaraciones de importacion
for j in range(total_paginas_importaciones):
    
    PaginaImagenImportacion = imagenpdfImportacion[j]

    # Recorta el cuadro especifico en la imagen
    cuadroImagenImportacion = PaginaImagenImportacion.crop((3350, 850, 4650, 1074))

    # Configuracion de solo numeros para una sola linea
    custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

    # Converimos la imagen a texto
    textImportacion = pytesseract.image_to_string(cuadroImagenImportacion, config=custom_config)

    if textImportacion == '':
        
        #cuadroImagenImportacion = PaginaImagen.crop((2980, 200, 4150, 420))
        
        # Configuracion de solo numeros para una sola linea
        #custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'

        # Converimos la imagen a texto
        #textSelectividad = pytesseract.image_to_string(cuadroImagenSelectividad, config=custom_config)
        numeros_de_importacion.append('respaldo')
    else:
        # Guardar los numeros de formularios en una lista
        numeros_de_importacion.append(textImportacion)

for j, numero_importacion in enumerate(numeros_de_importacion):
    print(f"j: {j}, numeros: {numero_importacion}")

organizar_pdfs(ruta_pdf_selectividades, ruta_pdf_importacion, numeros_de_selectividades, numeros_de_importacion, ruta_pdf_nuevo)

