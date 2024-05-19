from http.server import BaseHTTPRequestHandler
from urllib import parse

class handler(BaseHTTPRequestHandler):
  def do_GET(self):

    # Parse query
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    query_dict = dict(query_string_list)

    name = query_dict.get("name")


    #url_components = parse(path.query)

    # Response code
    self.send_response(200)

     # Establish header(s)
    self.send_header("Content-type", "text/plain")
    self.end_headers()

    #assemble payload message
    payload = f"hey there, {name}"

    #deploy payload to client requester
    self.wfile.write(payload.encode("utf-8"))
    return
