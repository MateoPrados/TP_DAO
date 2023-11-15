from reportlab.pdfgen import canvas
from db_entidades.database import Database
from db_entidades.db_libro import LibroDB

def generar_reporte_sumatoria_extraviados():

    database = Database()
    librodb = LibroDB(database)

    libros = librodb.listar_libros()


    pdf_filename = "reporte_sumatoria_extraviados.pdf"
    pdf = canvas.Canvas(pdf_filename)

    sumatoria = 0

    for libro in libros:
        if libro.estado.lower() == "extraviado":
            sumatoria += libro.precio_reposicion

    pdf.drawString(100, 800, "Reporte de Sumatoria de Precio de Reposición de Libros Extraviados")
    pdf.drawString(100, 780, f"Sumatoria: ${sumatoria}")

    pdf.save()


