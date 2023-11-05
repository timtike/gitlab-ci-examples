# test_main.py
import requests
import os
domain = os.getenv('DOMAIN', "localhost")

def test_read_root():
    print(f"domain is:{domain}")
    response = requests.get(f"http://{domain}:7200/")
    assert response.status_code == 200
    # assert response.json() == {"Hello": "World"}
