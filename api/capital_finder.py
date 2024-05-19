from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
  def do_GET(self):

    # Parse query, save as query_dict
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    query_dict = dict(query_string_list)

    #APIs TO SPEAK TO:
    country_api = "https://restcountries.com/v3.1/name/{name}"
    capital_api = "https://restcountries.com/v3.1/capital/{capital}"

    if "country" in query_dict.values():
      payload = requests.get(country_api + query_dict)

    if "capital" in query_dict.values():
      payload = requests.get(capital_api + query_dict)

    # Response code
    self.send_response(200)

     # Establish header(s)
    self.send_header("Content-type", "text/plain")
    self.end_headers()

    #assemble payload message
    payload = "No response. Did you give a value for country or capital?"

    #deploy payload to client requester
    self.wfile.write(payload.encode("utf-8"))
    return
