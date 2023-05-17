from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import cgi

# Define the request handler class
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Set the response status code
        self.send_response(200)

        # Set the response headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Parse the form data
        form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD': 'POST'}
        )

        # Check if the request contains a 'file' parameter in form data
        if 'file' in form:
            file_item = form['file']

            # Save the binary file in the current directory
            filename = os.path.basename(file_item.filename)
            with open(filename, 'wb') as f:
                f.write(file_item.file.read())
                print("Saved file:", filename)

        # Send a response back to the client
        response = "File received and saved."
        self.wfile.write(response.encode('utf-8'))

# Define the server host and port
host = '0.0.0.0'
port = 8000

# Create an HTTP server instance
server = HTTPServer((host, port), SimpleHTTPRequestHandler)

# Start the server
print("Server running on {}:{}".format(host, port))
server.serve_forever()
