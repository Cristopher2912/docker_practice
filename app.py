from http.server import BaseHTTPRequestHandler, HTTPServer
import os

COSAS = ["Docker", "Contenedores", "Imágenes"]


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        items = "".join(f"<li>{c}</li>" for c in COSAS)
        html = f"""<html><head><meta charset="utf-8"><title>Docker</title></head>
        <body><h1>Hola mundo desde Docker</h1><ul>{items}</ul></body></html>"""
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))


port = int(os.environ.get("PORT", 10000))
HTTPServer(("0.0.0.0", port), Handler).serve_forever()
