import requests

class GetRequester:
    def __init__(self, url):
        """Initialize with a URL string."""
        self.url = url

    def get_response_body(self):
        """
        Sends a GET request to the URL and returns the response body as a string.
        """
        response = requests.get(self.url)  # Send GET request
        return response.text  # Use response.text to get the body as a string

    def load_json(self):
        """
        Uses get_response_body to send a request, then parses the response body as JSON 
        and returns the Python object (list or dictionary).
        """
        response = requests.get(self.url)  # Send GET request
        return response.json()  # Parse and return the JSON response directly
