import unittest

from warpcast_server.tools import channel_tools
from warpcast_server import api as api_module


class MockAPI:
    async def follow_channel(self, name, follow=True):
        return {"ok": True}


class ChannelToolsTest(unittest.IsolatedAsyncioTestCase):
    async def test_follow_channel(self):
        api_module._api_client = MockAPI()
        result = await channel_tools.follow_channel("news")
        self.assertIn("now following", result.lower())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
