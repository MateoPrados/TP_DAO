from tkinter import messagebox
from reportlab.pdfgen import canvas
from db_entidades.database import Database
from db_entidades.db_libro import LibroDB
from db_entidades.db_prestamo import PrestamoDB


from tkinter.simpledialog import askstring

def generar_reporte_prestamos_socio(numero_socio=None):

    database = Database()
    dbprestamo = PrestamoDB(database)
    dblibro = LibroDB(database)

    if numero_socio is None:
        numero_socio = askstring("Número de Socio", "Ingrese el número de socio:")
    if numero_socio is None:
        return

    try:
        numero_socio = int(numero_socio)
    except ValueError:
        messagebox.showerror("Error", "El número de socio debe ser un número entero.")
        return

    prestamos = dbprestamo.listar_prestamos()
    prestamos_de_socio = []

    for prestamo in prestamos:
        if prestamo.socio == numero_socio:
            prestamos_de_socio.append(prestamo)

    pdf_filename = f"reporte_prestamossocio{numero_socio}.pdf"
    pdf = canvas.Canvas(pdf_filename)

    pdf.drawString(100, 800, f"Reporte de Préstamos del Socio '{numero_socio}'")
    pdf.drawString(100, 780, "Préstamos:")

    y_position = 760
    for prestamo in prestamos_de_socio:
        libro = dblibro.obtener_libro_por_codigo(prestamo.libro)
        if libro:
                pdf.drawString(120, y_position, f"- Libro: {libro.titulo}, Fecha de Préstamo: {prestamo.fecha_prestamo}")
        else:
            pdf.drawString(120, y_position, f"- Libro no encontrado, ID: {prestamo.libro}, Fecha de Préstamo: {prestamo.fecha_prestamo}")
        y_position -= 20

    pdf.save()