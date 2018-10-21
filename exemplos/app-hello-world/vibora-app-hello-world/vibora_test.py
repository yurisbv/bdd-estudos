from vibora.tests import TestSuite
from app import app
import json


class HelloWorldTestCase(TestSuite):
    
    def setUp(self):
        self.client = app.test_client()

    async def test_endpoint(self, verb, endpoint, result):
        if verb.lower() == 'get':
            return await self.client.get(endpoint)
            # return self.assertEqual(response.content, result)