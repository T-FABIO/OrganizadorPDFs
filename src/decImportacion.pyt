from pdf2image import convert_from_path
from PyPDF2 import PdfReader, PdfWriter
from PIL import Image
import pytesseract

# Configurar la ruta al ejecutable de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

ruta_pdf_selectividades = r'C:\Users\USUARIO\Desktop\Programacion\Python\Practica\PDFs\Selectividades.pdf'

# lista de numeros de formularios
numeros_de_formularios = []

def obtener_total_paginas(ruta_pdf):
    # Crear un objeto PdfReader para leer el PDF
    lector_pdf = PdfReader(ruta_pdf)
    
    # Obtener el número total de páginas
    total_paginas = len(lector_pdf.pages)
    
    return total_paginas

total_paginas = obtener_total_paginas(ruta_pdf_selectividades)
print(total_paginas)
# Convierte el pdf a imagenes
imagenPdfSelectividad = convert_from_path(ruta_pdf_selectividades, 600)