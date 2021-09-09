#!/usr/bin/python3
# Set the path to your python3 above

import requests

def run():
    
    result = requests.get("http://www.google.com")
    print(result.text)


if __name__ == "__main__":
    run()
