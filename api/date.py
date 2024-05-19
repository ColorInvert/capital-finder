from http.server import BaseHTTPRequestHandler


class handler(BaseHTTPRequestHandler):
  def do_GET(self):

    # Response code
    self.send_response(200)

     # Establish header(s)
    self.send_header("Content-type", "text/plain")
    self.end_headers()

    self.wfile.write("Hello, world!".encode("utf-8"))
    return
