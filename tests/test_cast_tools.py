import unittest

from warpcast_server.tools import cast_tools
from warpcast_server import api as api_module


class MockAPI:
    async def post_cast(self, text, parent_cast_id=None):
        return {"url": "fake"}


class CastToolsTest(unittest.IsolatedAsyncioTestCase):
    async def test_post_cast(self):
        api_module._api_client = MockAPI()
        result = await cast_tools.post_cast("hello")
        self.assertIn("fake", result)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
