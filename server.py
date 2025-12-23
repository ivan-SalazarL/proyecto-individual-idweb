"""
ARCHIVO: servidor.py
DESCRIPCIÓN: Servidor web backend basado en HTTP nativo de Python.
            Gestiona rutas, archivos estáticos y conexión a base de datos MySQL.
AUTOR: Iván Salazar Luque
"""

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import mysql.connector

# Configuración de red del servidor
HOST = "localhost"
PORT = 8000

# Configuración de conexión para MySQL
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "", 
    "database": "idweb_proyecto"
}

# Credencial para el acceso al panel de administración
ADMIN_PASSWORD = "admin123"

class MiServidor(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"

        if self.path.startswith("/admin"):
            self.mostrar_admin()
            return

        try:
            ruta = "." + self.path
            with open(ruta, "rb") as archivo:
                self.send_response(200)

                if ruta.endswith(".html"):
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                elif ruta.endswith(".css"):
                    self.send_header("Content-Type", "text/css")
                elif ruta.endswith(".js"):
                    self.send_header("Content-Type", "application/javascript")
                elif ruta.endswith(".jpg") or ruta.endswith(".jpeg"):
                    self.send_header("Content-Type", "image/jpeg")
                elif ruta.endswith(".png"):
                    self.send_header("Content-Type", "image/png")
                elif ruta.endswith(".webp"):
                    self.send_header("Content-Type", "image/webp")
                else:
                    self.send_header("Content-Type", "application/octet-stream")

                self.end_headers()
                self.wfile.write(archivo.read())

        except FileNotFoundError:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Archivo no encontrado")

    def do_POST(self):
        if self.path == "/contacto":
            self.guardar_mensaje()
        elif self.path == "/admin":
            self.verificar_admin()

    def guardar_mensaje(self):
        longitud = int(self.headers.get("Content-Length", 0))
        datos = self.rfile.read(longitud).decode("utf-8")
        formulario = parse_qs(datos)

        nombre = formulario.get("nombre", [""])[0]
        email = formulario.get("email", [""])[0]
        mensaje = formulario.get("mensaje", [""])[0]

        conexion = mysql.connector.connect(**DB_CONFIG)
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO mensajes (nombre,email,mensaje) VALUES (%s,%s,%s)",
            (nombre, email, mensaje)
        )
        conexion.commit()
        cursor.close()
        conexion.close()

        html = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
          <meta charset="utf-8">
          <title>Mensaje enviado</title>
          <link rel="stylesheet" href="/css/estilos.css">
        </head>
        <body>
            <main style="text-align:center; padding:80px;">
              <h2>Mensaje recibido</h2>
              <p>Gracias por compartirlo.</p>
              <a href="/vida.html" class="btn-respuesta">Volver</a>
            </main>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def mostrar_admin(self):
        html = """
        <!DOCTYPE html>
        <html lang="es">
        <head>
          <meta charset="utf-8">
          <title>Área privada</title>
          <link rel="stylesheet" href="/css/estilos.css">
        </head>
        <body>
            <main style="text-align:center; padding:80px;">
              <h2>Área privada</h2>
              <form method="POST" action="/admin">
                <input type="password" name="password" placeholder="Contraseña" style="width:100%; max-width:300px;">
                <br><br>
                <button class="btn-respuesta">Entrar</button>
              </form>
              <br>
              <a href="/index.html" class="btn-respuesta">Volver al inicio</a>
            </main>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

    def verificar_admin(self):
        longitud = int(self.headers.get("Content-Length", 0))
        datos = self.rfile.read(longitud).decode("utf-8")
        formulario = parse_qs(datos)
        password = formulario.get("password", [""])[0]

        if password != ADMIN_PASSWORD:
            self.send_response(200) 
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            
            error_html = """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="utf-8">
                <link rel="stylesheet" href="/css/estilos.css">
                <title>Acceso Denegado</title>
            </head>
            <body>
                <header>
                    <h1>Área Restringida</h1>
                </header>
                <main style="text-align:center; padding:60px;">
                    <h2 style="color: #ff4f4f; border-left: none; padding:0;">Acceso Denegado</h2>
                    <p style="font-style: italic; font-size: 1.3em; color: #ffffff; margin: 25px 0;">
                        "No todo lo bueno se muestra a simple vista..."
                    </p>
                    <p>La clave es incorrecta. Por favor, verifica tus credenciales.</p>
                    <br>
                    <a href="/admin" class="btn-respuesta">Reintentar</a>
                </main>
            </body>
            </html>
            """
            self.wfile.write(error_html.encode("utf-8"))
            return

        # Si la clave es correcta, mostramos la tabla
        conexion = mysql.connector.connect(**DB_CONFIG)
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre,email,mensaje,fecha FROM mensajes ORDER BY fecha DESC")
        mensajes = cursor.fetchall()
        cursor.close()
        conexion.close()

        filas = ""
        for n, e, m, f in mensajes:
            filas += f"<tr><td>{n}</td><td>{e}</td><td>{m}</td><td>{f}</td></tr>"

        html = f"""
        <!DOCTYPE html>
        <html lang="es">
        <head>
          <meta charset="utf-8">
          <title>Mensajes Recibidos</title>
          <link rel="stylesheet" href="/css/estilos.css">
        </head>
        <body>
            <header><h1>Panel Administrativo</h1></header>
            <main>
              <h2>Registro de Recomendaciones</h2>
              <table class="tabla">
                <tr><th>Nombre</th><th>Email</th><th>Mensaje</th><th>Fecha</th></tr>
                {filas}
              </table>
              <br>
              <div style="text-align:center;">
                <a href="/index.html" class="btn-respuesta">Cerrar Sesión</a>
              </div>
            </main>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

if __name__ == "__main__":
    print(f"Servidor iniciado en http://{HOST}:{PORT}")
    HTTPServer((HOST, PORT), MiServidor).serve_forever()