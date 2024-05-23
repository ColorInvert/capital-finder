from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        # assemble default payload message
        payload = (
            "This message not modified. Did you give a value for country or capital?"
        )

        # Parse query, save as query_dict
        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        query_dict = dict(query_string_list)

        # APIs TO SPEAK TO:
        country_api = "https://restcountries.com/v3.1/name/{name}"
        capital_api = "https://restcountries.com/v3.1/capital/{capital}"

        # if user provides a ?country=x then call the v3.1/name/x url.
        if "country" in query_dict.keys():
            payload = "USAGE OF COUNTRY KEYWORD DETECTED, BUT RESPONSE NOT ASSEMBLED."

            try:
                response = requests.get(country_api.format(name=query_dict["country"]))
                if response.status_code == 200:
                    data = response.json()
                    print(f"OUR DATA IS {data}")
                    answer = []

            except:
                response.raise_for_status()

            for countries in data:
                country = countries["capital"][0]

                answer.append(country)
            payload = f"The capital of {query_dict['country']} is {str(answer[0])}."

        # If user provides a ?capital=y then call the v3.1/capital/y url.
        if "capital" in query_dict.keys():
            payload = "USAGE OF CAPITAL KEYWORD DETECTED, BUT RESPONSE NOT ASSEMBLED."
            try:

                response = requests.get(
                    capital_api.format(capital=query_dict["capital"])
                )
                if response.status_code == 200:
                    data = response.json()
                    print(f"OUR DATA IS {data}")
                    answer = []

            except:
                response.raise_for_status()

            # print(f"DATA IS {data[0]['name']['common']}")
            for capitals in data:
                capital = capitals["capital"][0]

                answer.append(capital)
            # answer.append(data[0]['name']['common'])
            payload = f"{query_dict['capital']} is the capital of {str(answer[0])}."

        # Parse through ocean of data in response, extract only the opposite of request
        # IE, capital data if country input, country data if capital input.

        # Response code
        self.send_response(200)

        # Establish header(s)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        # deploy payload to client requester
        self.wfile.write(payload.encode("utf-8"))
        return
