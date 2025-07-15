import unittest
from mutations import apply_mutations

class TestReconForge(unittest.TestCase):

    def test_depth_1(self):
        result = apply_mutations(['test'], depth=1)
        self.assertIn('test', result)
        self.assertIn('TEST', result)

    def test_depth_3(self):
        result = apply_mutations(['test'], depth=3, dob="23031995", extra_dates=["14022018"])
        self.assertTrue(any("@" in r or r[::-1] == 'test' for r in result))

    def test_depth_5(self):
        result = apply_mutations(['test'], depth=5, dob="23031995", extra_dates=["14022018"])
        self.assertTrue(any("!@#" in r or "$$" in r or "_" in r for r in result))

if __name__ == "__main__":
    unittest.main()
