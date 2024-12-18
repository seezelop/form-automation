import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from dotenv import load_dotenv

# Cargar las credenciales desde .env
load_dotenv()
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')

# Función parametrizada para invocar desde Flask/React
def enviar_correo_param(correo, asunto, mensaje, archivo_ruta):
    # Configuración del correo
    remitente = EMAIL_USER
    destinatario = correo
    cuerpo = mensaje

    # Crear el mensaje
    mensaje_email = MIMEMultipart()
    mensaje_email['From'] = remitente
    mensaje_email['To'] = destinatario
    mensaje_email['Subject'] = asunto

    # Agregar el cuerpo del mensaje
    mensaje_email.attach(MIMEText(cuerpo, 'plain'))

    # Adjuntar el archivo
    try:
        with open(archivo_ruta, "rb") as adjunto:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload(adjunto.read())
            encoders.encode_base64(parte)
            parte.add_header(
                'Content-Disposition',
                f'attachment; filename={archivo_ruta}',
            )
            mensaje_email.attach(parte)
    except Exception as e:
        raise Exception(f"Error al adjuntar el archivo: {e}")

    # Enviar el correo
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL_USER, EMAIL_PASS)
        servidor.sendmail(remitente, destinatario, mensaje_email.as_string())
        servidor.quit()
        print("Correo enviado exitosamente.")
    except Exception as e:
        raise Exception(f"Error al enviar el correo: {e}")


# Función existente para ejecutar desde la terminal
def enviar_correo():
    # Configuración del correo
    remitente = EMAIL_USER
    destinatario = "selopez@teco.com.ar"  # Cambia al correo del destinatario
    asunto = "Reporte de análisis automático"
    cuerpo = "Adjunto encontrarás el reporte de análisis de datos generado automáticamente."

    # Crear el mensaje
    mensaje_email = MIMEMultipart()
    mensaje_email['From'] = remitente
    mensaje_email['To'] = destinatario
    mensaje_email['Subject'] = asunto

    # Agregar el cuerpo del mensaje
    mensaje_email.attach(MIMEText(cuerpo, 'plain'))

    # Nombre del archivo adjunto
    nombre_archivo = "resultado_analisis.xlsx"

    # Adjuntar el archivo
    try:
        with open(nombre_archivo, "rb") as adjunto:
            parte = MIMEBase('application', 'octet-stream')
            parte.set_payload(adjunto.read())
            encoders.encode_base64(parte)
            parte.add_header(
                'Content-Disposition',
                f'attachment; filename={nombre_archivo}',
            )
            mensaje_email.attach(parte)
    except Exception as e:
        print(f"Error al adjuntar el archivo: {e}")
        return

    # Enviar el correo
    try:
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(EMAIL_USER, EMAIL_PASS)
        servidor.sendmail(remitente, destinatario, mensaje_email.as_string())
        servidor.quit()
        print("Correo enviado exitosamente.")
    except Exception as e:
        print(f"Error al enviar el correo: {e}")


# Prueba directa desde la terminal
if __name__ == "__main__":
    enviar_correo()
