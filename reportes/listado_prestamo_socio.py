from reportlab.pdfgen import canvas
from db_entidades.database import Database
from db_entidades.db_libro import LibroDB
from db_entidades.db_prestamo import PrestamoDB


def generar_reporte_prestamos_socio(numero_socio):

    database = Database()
    dbprestamo = PrestamoDB(database)
    dblibro = LibroDB(database)
    prestamos = dbprestamo.listar_prestamos()

    prestamos_de_socio = []

    for prestamo in prestamos:
        if prestamo.socio == numero_socio:
            prestamos_de_socio.append(prestamo)

    pdf_filename = f"reporte_prestamos_socio_{numero_socio}.pdf"
    pdf = canvas.Canvas(pdf_filename)


    pdf.drawString(100, 800, f"Reporte de Préstamos del Socio '{numero_socio}'")
    pdf.drawString(100, 780, "Préstamos:")
    
    y_position = 760
    for prestamo in prestamos_de_socio:
        libro = dblibro.obtener_libro_por_codigo(prestamo.libro)
        pdf.drawString(120, y_position, f"- Libro: {libro.titulo}, Fecha de Préstamo: {prestamo.fecha_prestamo}")
        y_position -= 20

    pdf.save()

