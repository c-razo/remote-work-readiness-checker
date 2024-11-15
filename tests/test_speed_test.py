import unittest
from features.speed_test import internet_speed_test

class TestInternetSpeedTest(unittest.TestCase):
    def test_internet_speed_test(self):
        results = internet_speed_test()
        
        # Check if the keys exist in the output
        self.assertIn("Download Speed", results)
        self.assertIn("Upload Speed", results)
        self.assertIn("Ping", results)
        
        # Ensure results are in string format with units
        self.assertIsInstance(results["Download Speed"], str)
        self.assertTrue("Mbps" in results["Download Speed"])
        self.assertIsInstance(results["Upload Speed"], str)
        self.assertTrue("Mbps" in results["Upload Speed"])
        self.assertIsInstance(results["Ping"], str)
        self.assertTrue("ms" in results["Ping"])

if __name__ == "__main__":
    unittest.main()

