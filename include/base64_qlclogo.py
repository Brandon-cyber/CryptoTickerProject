import base64

with open ("/Users/brandonsoukup/PycharmProjects/BTCTicker/venv/include/qlclogo.gif", "r+b") as image_file:
    base64_qlc = base64.b64encode(image_file.read())