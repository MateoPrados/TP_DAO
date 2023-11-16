from tkinter.simpledialog import askstring
from reportlab.pdfgen import canvas
from db_entidades.database import Database
from db_entidades.db_prestamo import PrestamoDB

def generar_reporte_solicitantes_libro(titulo_libro=None):

    database = Database()
    dbprestamo = PrestamoDB(database)

    if titulo_libro is None:
        titulo_libro = askstring("Título del Libro", "Ingrese el título del libro:")
    if titulo_libro is None:
        return

    solicitantes = dbprestamo.obtener_solicitantes_por_titulo(titulo_libro)

    pdf_filename = f"reporte_solicitanteslibro{titulo_libro}.pdf"
    pdf = canvas.Canvas(pdf_filename)

    pdf.drawString(100, 800, f"Reporte de Solicitantes del Libro '{titulo_libro}'")
    pdf.drawString(100, 780, "Solicitantes:")

    y_position = 760
    for solicitante in solicitantes:
        pdf.drawString(120, y_position, f"- {solicitante}")
        y_position -= 20

    pdf.save()

