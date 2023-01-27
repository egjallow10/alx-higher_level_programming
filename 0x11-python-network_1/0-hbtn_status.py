#!/usr/bin/python3
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode())

