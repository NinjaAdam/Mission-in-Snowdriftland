import http.server
import socketserver
import os

# Define the port on which you want to serve the HTML file
PORT = 8000

# Define the directory where index.html is located (use current directory)
web_dir = os.path.join(os.path.dirname(__file__), '')
os.chdir(web_dir)

# Create a request handler for serving the files
Handler = http.server.SimpleHTTPRequestHandler

# Set up the server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}. Open http://localhost:{PORT} to view.")
    # Start the server
    httpd.serve_forever()
