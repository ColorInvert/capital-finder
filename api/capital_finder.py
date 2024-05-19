from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
  def do_GET(self):

    #assemble default payload message
    payload = "This message not modified. Did you give a value for country or capital?"


    # Parse query, save as query_dict
    path = self.path
    url_components = parse.urlsplit(path)
    query_string_list = parse.parse_qsl(url_components.query)
    query_dict = dict(query_string_list)

    #APIs TO SPEAK TO:
    country_api = "https://restcountries.com/v3.1/name/{name}"
    capital_api = "https://restcountries.com/v3.1/capital/{capital}"



    #if user provides a ?country=x then call the v3.1/name/x url.
    if "country" in query_dict.keys():
      response = requests.get(country_api + query_dict["country"])
      data = response.json()

      answer = []

      payload = "USAGE OF COUNTRY KEYWORD DETECTED, BUT RESPONSE NOT ASSEMBLED."

      
      answer.append(data['capital'][0])
      payload = f"The capital of {query_dict["country"]} is {str(answer)}."

    # If user provides a ?capital=y then call the v3.1/capital/y url.
    if "capital" in query_dict.keys():
      response = requests.get(capital_api + query_dict["capital"])
      data = response.json()

      answer = []

      payload = "USAGE OF CAPITAL KEYWORD DETECTED, BUT RESPONSE NOT ASSEMBLED."

      answer.append(data['country'][0])
      payload = f"{query_dict["capital"]} is the capital of {str(answer)}."
      

    # Parse through ocean of data in response, extract only the opposite of request
    # IE, capital data if country input, country data if capital input.




    # Response code
    self.send_response(200)

     # Establish header(s)
    self.send_header("Content-type", "text/plain")
    self.end_headers()

    #deploy payload to client requester
    self.wfile.write(payload.encode("utf-8"))
    return
