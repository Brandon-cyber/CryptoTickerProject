import base64

with open ("/Users/brandonsoukup/PycharmProjects/BTCTicker/venv/include/btclogo.gif", "r+b") as image_file:
    base64_btc = base64.b64encode(image_file.read())