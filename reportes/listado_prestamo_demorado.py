from reportlab.pdfgen import canvas
from datetime import datetime
from db_entidades.database import Database
from db_entidades.db_prestamo import PrestamoDB


def calcular_demora(fecha_devolucion_pactada, fecha_devolucion):
    fecha_pactada = datetime.strptime(fecha_devolucion_pactada, "%d/%m/%Y")  
    fecha_devolucion = datetime.strptime(fecha_devolucion, "%d/%m/%Y")  
    return (fecha_devolucion - fecha_pactada).days

def generar_reporte_prestamos_demorados():

    database = Database()
    dbprestamo = PrestamoDB(database)
    prestamos_demorados = dbprestamo.obtener_prestamos_demorados()
    print(prestamos_demorados)

    pdf_filename = "reporte_prestamos_demorados.pdf"
    pdf = canvas.Canvas(pdf_filename)

    pdf.drawString(100, 800, "Reporte de Préstamos Demorados")
    pdf.drawString(100, 780, "Préstamos Demorados:")
    
    y_position = 760
    for prestamo in prestamos_demorados:
        if (prestamo[4] < prestamo[5]):

            demora = calcular_demora(prestamo[4], prestamo[5])
            pdf.drawString(120, y_position, f"- Libro: {prestamo[0]}, Solicitante: {prestamo[2]}, Demora:{demora} días")
            y_position -= 20

    pdf.save()
