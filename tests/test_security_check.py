import unittest
from features.security_check import system_security_check

class TestSystemSecurityCheck(unittest.TestCase):
    def test_system_security_check(self):
        results = system_security_check()
        
        # Check if the essential keys exist in the output
        self.assertIn("Operating System", results)
        self.assertIn("Password Strength", results)
        self.assertIn("Firewall", results)
        self.assertIn("Software Updates", results)
        self.assertIn("Antivirus", results)
        self.assertIn("2FA", results)
        
        # Check for reasonable responses
        self.assertIsInstance(results["Operating System"], str)
        self.assertIsInstance(results["Password Strength"], str)

if __name__ == "__main__":
    unittest.main()

