
from reportlab.pdfgen import canvas
from db_entidades.database import Database
from db_entidades.db_libro import LibroDB

def generar_reporte_estado_libros():

    database = Database()
    librodb = LibroDB(database)

    libros = librodb.listar_libros()

    pdf_filename = "reporte_estado_libros.pdf"
    pdf = canvas.Canvas(pdf_filename)

    estados = {"disponible": 0, "prestado": 0, "extraviado": 0}

    for libro in libros:
        estados[libro.estado.lower()] += 1

    pdf.drawString(100, 800, "Reporte de Cantidad de Libros por Estado")
    pdf.drawString(100, 780, f"Libros Disponibles: {estados['disponible']}")
    pdf.drawString(100, 760, f"Libros Prestados: {estados['prestado']}")
    pdf.drawString(100, 740, f"Libros Extraviados: {estados['extraviado']}")

    pdf.save()

    
