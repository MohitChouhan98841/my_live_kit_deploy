import http.server
import ssl

# Set the directory where your web files are located
web_dir = "/"  # Replace with your actual web directory path

# Create an HTTP server that serves files from `web_dir`
httpd = http.server.HTTPServer(('0.0.0.0', 8000), http.server.SimpleHTTPRequestHandler)
# Wrap the server with SSL, providing your self-signed cert and key
httpd.socket = ssl.wrap_socket(httpd.socket,
                            #    keyfile="./keys/new_kyes/private.key",  # Path to your private key
                            #    certfile="./keys/new_kyes/server.crt",  # Path to your certificate
                               keyfile="./keys/server.key",  # Path to your private key
                               certfile="./keys/server.crt",  # Path to your certificate
                               server_side=True)

print("Serving HTTPS on https://localhost:8000")
httpd.serve_forever()
