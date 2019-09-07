import base64

with open ("/Users/brandonsoukup/PycharmProjects/BTCTicker/venv/include/powrlogo.gif", "r+b") as image_file:
    base64_powr = base64.b64encode(image_file.read())