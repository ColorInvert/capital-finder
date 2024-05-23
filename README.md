# Serverless Functions

## A first exploration of serverless functions using vercel, python, and the restcountries.com API.

### By Casey Glidewell

#### What it is

serverless, or capital_finder.py is a first foray into usage of serverless functions. It is hosted on Vercel, and if provided with a string argument for a capital name or country name, it will ping restcountries.com, format the json received, and return to the user a simple line of text telling them what the respective capital or country is for their input.

##### How to use

To receive the country a capital is located within, format the url like so:
https://capital-finder-casey-g.vercel.app/api/capital_finder?country=vietnam

To receive the capital of an input country, format the url like so:
https://capital-finder-casey-g.vercel.app/api/capital_finder?capital=hanoi

The two examples above can have the contents after the = sign replaced with your own country or capital name to receive the expected results for that country or capital.