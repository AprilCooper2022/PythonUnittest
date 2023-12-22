
from flask import Flask
from flask.testing import FlaskClient
import unittest
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
        return 'Hello, World!'

class TestApp(unittest.TestCase):

    def setUp(self):
        # Create a test client
        self.app = app.test_client()

    def test_hello_world(self):
        # Test the root route ("/")
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')
    
    def test_website_load(self):
        # Define the URL to test
        url = 'https://atg.world/'

        # Print a log statement indicating the start of the test
        print("Testing if the website loads properly...")

        # Make an HTTP GET request to the website
        response = requests.get(url)

       # Check if the response status code is 200 (OK)
        if response.status_code == 200:
           # Print a log statement indicating a successful load
           print("Website loaded successfully! Status Code: 200")
        else:
           # Print a log statement indicating a failed load
           print(f"Failed to load the website. Status Code: {response.status_code}")
           # Fail the test with an appropriate message
           self.fail("Website did not load properly.")

if __name__ == '__main__':
    # Run the Flask application in debug mode
    app.run(debug=True, host='0.0.0.0')
    # Run the tests
    unittest.main()

