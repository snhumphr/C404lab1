#!/usr/bin/python3
# Set the path to your python3 above

import requests

def run():
    
    result = requests.get("https://raw.githubusercontent.com/snhumphr/C404lab1/main/lab1.py")
    print(result.text)


if __name__ == "__main__":
    run()
