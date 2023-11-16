from reportlab.pdfgen import canvas
from db_entidades.database import Database
from db_entidades.db_libro import LibroDB
import matplotlib.pyplot as plt
import tempfile

def generar_reporte_estado_libros():
    database = Database()
    librodb = LibroDB(database)
    libros = librodb.listar_libros()

    pdf_filename = "reporte_estado_libros.pdf"
    pdf = canvas.Canvas(pdf_filename)

    estados = {"disponible": 0, "prestado": 0, "extraviado": 0}
    for libro in libros:
        estados[libro.estado.lower()] += 1

    plt.bar(estados.keys(), estados.values())
    plt.title("Estado de Libros")
    plt.xlabel("Estado")
    plt.ylabel("Cantidad")

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    plt.savefig(temp_file.name, format='png')
    temp_file.close()

    pdf.drawInlineImage(temp_file.name, 100, 300, width=400, height=300)

    pdf.drawString(100, 710, "Reporte de Cantidad de Libros por Estado")
    pdf.drawString(100, 690, f"Libros Disponibles: {estados['disponible']}")
    pdf.drawString(100, 670, f"Libros Prestados: {estados['prestado']}")
    pdf.drawString(100, 650, f"Libros Extraviados: {estados['extraviado']}")

    pdf.save()