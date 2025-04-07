from GetRequester import GetRequester

# Constants
URL = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
JSON_STRING = b"[\n  {\n    \"name\": \"Daniel\",\n    \"occupation\": \"LG Fridge Salesman\"\n  },\n  {\n    \"name\": \"Joe\",\n    \"occupation\": \"WiFi Fixer\"\n  },\n  {\n    \"name\": \"Avi\",\n    \"occupation\": \"DJ\"\n  },\n  {\n    \"name\": \"Howard\",\n    \"occupation\": \"Mountain Legend\"\n  }\n]\n"
CONVERTED_DATA = [
    { 'name': 'Daniel', 'occupation': 'LG Fridge Salesman' },
    { 'name': 'Joe', 'occupation': 'WiFi Fixer' },
    { 'name': 'Avi', 'occupation': 'DJ' },
    { 'name': 'Howard', 'occupation': 'Mountain Legend' }
]

# Test for raw byte response
def test_get_response():
    '''get_response_body function returns byte response.'''
    requester = GetRequester(URL)
    assert requester.get_response_body() == JSON_STRING.decode()  # decoding bytes for string comparison

# Test for parsed JSON object
def test_load_json():
    '''load_json function returns a list of dictionaries.'''
    requester = GetRequester(URL)
    assert requester.load_json() == CONVERTED_DATA
