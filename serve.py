#!/usr/bin/env python3
import http.server
import socketserver
import webbrowser
import sys

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

class MyTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run():
    print(f"Starting server on port {PORT}...")
    print(f"Opening browser at http://localhost:{PORT}/index.html")
    
    # Try to open browser automatically
    try:
        webbrowser.open(f"http://localhost:{PORT}/index.html")
    except Exception as e:
        print(f"Could not open browser automatically: {e}")

    try:
        with MyTCPServer(("", PORT), Handler) as httpd:
            print("Server running. Press Ctrl+C to stop.")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server.")
        sys.exit(0)
    except OSError as e:
        print(f"Error starting server: {e}")
        print("Port might be in use. Try running on another port or check running processes.")
        sys.exit(1)

if __name__ == "__main__":
    run()
