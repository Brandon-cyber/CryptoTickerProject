import base64

with open ("/Users/brandonsoukup/PycharmProjects/BTCTicker/venv/include/background.gif", "r+b") as image_file:
    base64_background = base64.b64encode(image_file.read())