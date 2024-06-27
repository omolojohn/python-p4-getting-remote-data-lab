import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return json.loads(response_body)

# Test classes
class GetRequesterTest:
    '''Class {Classname} in {modulename}.py'''

URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = [
    {'name': 'Daniel', 'occupation': 'LG Fridge Salesman'},
    {'name': 'Joe', 'occupation': 'WiFi Fixer'},
    {'name': 'Avi', 'occupation': 'DJ'},
    {'name': 'Howard', 'occupation': 'Mountain Legend'}
]

def test_get_response():
    '''get_response_body function returns response.'''
    requester = GetRequester(URL)
    assert(requester.get_response_body() == JSON_STRING.decode('utf-8'))

def test_load_json():
    '''load_json function returns response.'''
    requester = GetRequester(URL)
    assert(requester.load_json() == CONVERTED_DATA)
