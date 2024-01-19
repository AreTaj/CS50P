# Bitcoin Price Index
# Problem Set 4

# https://api.coindesk.com/v1/bpi/currentprice.json

import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit("Missing command line argument")
else:
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    # print(json.dumps(request.json(), indent = 2))
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command line argument is not a number")

    data = request.json()
    price = data["bpi"]["USD"]["rate_float"]
    price = float(price) * float(sys.argv[1])
    print(f"${price:,.4f}")