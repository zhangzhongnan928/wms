import unittest

from warpcast_server.utils import validate_cast_text


class ValidatorsTest(unittest.TestCase):
    def test_validate_cast_text(self):
        self.assertTrue(validate_cast_text("hello"))
        self.assertFalse(validate_cast_text("a" * 321))


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
