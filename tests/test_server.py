import unittest

import warpcast_server


class ServerTest(unittest.TestCase):
    def test_tools_registered(self):
        self.assertIn("post_cast", warpcast_server.mcp.tools)
        self.assertIn("get_channel", warpcast_server.mcp.tools)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
