import unittest

from warpcast_server.api import WarpcastAPI


class MockResponse:
    def __init__(self, data):
        self._data = data
        self.status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return self._data


class MockClient:
    async def post(self, url, json=None):
        return MockResponse({"url": "https://warpcast.com/cast/1"})

    async def get(self, url, params=None):
        return MockResponse({"casts": []})


class APITest(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.api = WarpcastAPI("token")
        self.api.client = MockClient()

    async def test_post_cast(self):
        data = await self.api.post_cast("hello")
        self.assertEqual(data["url"], "https://warpcast.com/cast/1")

    async def test_get_user_casts(self):
        data = await self.api.get_user_casts("user")
        self.assertEqual(data["casts"], [])


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
