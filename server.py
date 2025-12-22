from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import mysql.connector
import os

HOST = "localhost"
PORT = 8000

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "idweb_proyecto"
}

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

        sql = "INSERT INTO mensajes (nombre, email, mensaje) VALUES (%s, %s, %s)"
        valores = (nombre, email, mensaje)
        cursor.execute(sql, valores)

        conexion.commit()
        cursor.close()
        conexion.close()

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        respuesta = """
        <html>
        <head><meta charset="utf-8"></head>
        <body style="background:#0f1218;color:#d0d6e0;font-family:Arial;text-align:center;padding:50px;">
            <h2>Gracias por dejarlo aquí.</h2>
            <p>Tu recomendación fue recibida.</p>
            <a href="/vida.html" style="color:#9bb1ff;">Volver</a>
        </body>
        </html>
        """

        self.wfile.write(respuesta.encode("utf-8"))

    def mostrar_admin(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()

        html = """
        <html>
        <head><meta charset="utf-8"></head>
        <body style="background:#0f1218;color:#d0d6e0;font-family:Arial;text-align:center;padding:60px;">
            <h2>Área protegida</h2>
            <form method="POST" action="/admin">
                <input type="password" name="password" placeholder="Contraseña"
                       style="padding:10px;border-radius:8px;border:none;">
                <br><br>
                <button type="submit"
                        style="padding:10px 20px;border:none;border-radius:8px;background:#2a3140;color:#fff;">
                    Entrar
                </button>
            </form>
        </body>
        </html>
        """

        self.wfile.write(html.encode("utf-8"))

    def verificar_admin(self):
        longitud = int(self.headers.get("Content-Length", 0))
        datos = self.rfile.read(longitud).decode("utf-8")
        formulario = parse_qs(datos)

        password = formulario.get("password", [""])[0]

        if password != ADMIN_PASSWORD:
            self.send_response(403)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"<h2>Acceso denegado</h2>")
            return

        conexion = mysql.connector.connect(**DB_CONFIG)
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre, email, mensaje, fecha FROM mensajes ORDER BY fecha DESC")
        mensajes = cursor.fetchall()

        cursor.close()
        conexion.close()

        html = """
        <html>
        <head>
        <meta charset="utf-8">
        <style>
            body { background:#0f1218;color:#d0d6e0;font-family:Arial;padding:40px; }
            table { width:100%;border-collapse:collapse; }
            th, td { padding:12px;border-bottom:1px solid #2a3140;text-align:left; }
            th { background:#1a1f2a; }
        </style>
        </head>
        <body>
        <h2>Mensajes recibidos</h2>
        <table>
            <tr>
                <th>Nombre</th>
                <th>Email</th>
                <th>Mensaje</th>
                <th>Fecha</th>
            </tr>
        """

        for nombre, email, mensaje, fecha in mensajes:
            html += f"""
            <tr>
                <td>{nombre}</td>
                <td>{email}</td>
                <td>{mensaje}</td>
                <td>{fecha}</td>
            </tr>
            """

        html += """
        </table>
        <br><br>
<div style="text-align:center;">
  <a href="/vida.html"
     style="
       background:#2a3140;
       color:#fff;
       padding:10px 20px;
       border-radius:12px;
       text-decoration:none;
       display:inline-block;
     ">
    Volver al sitio
  </a>
</div>

        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    servidor = HTTPServer((HOST, PORT), MiServidor)
    print(f"Servidor corriendo en http://{HOST}:{PORT}")
    servidor.serve_forever()
