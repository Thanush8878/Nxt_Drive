import http.server
import socketserver
import webbrowser
import os

PORT = 8080
DIRECTORY = os.path.join(os.path.dirname(__file__), "web_preview")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    print(f"[*] Starting DriveMate Demo Server at http://localhost:{PORT}")
    webbrowser.open(f"http://localhost:{PORT}/index.html")
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server stopped.")

if __name__ == "__main__":
    run()
