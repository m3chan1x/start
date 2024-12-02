from http.client import responses

import requests


def create_object():
   payload = {
      "name": "Apple MacBook Pro 16",
      "data": {
         "year": 2019,
         "price": 1849.99,
         "CPU model": "Intel Core i9",
         "Hard disk size": "1 TB"
      }
   }
   response = requests.post('https://api.restful-api.dev/objects', json=payload).json()

def get_response():
   response = requests.get('https://api.restful-api.dev/objects/ff808181932badb60193887d79846ff4').json()

def update_object():
   payload = {
         "name": "Apple MacBook Pro 20",
         "data": {
            "year": 2020,
            "price": 7777,
            "CPU model": "M10",
            "Hard disk size": "1 TB"
         }
      }
   response = requests.put('https://api.restful-api.dev/objects/ff808181932badb60193887d79846ff4', json = payload).json()

def delete_object():
   response = requests.delete('https://api.restful-api.dev/objects/ff808181932badb60193887d79846ff4').json()




