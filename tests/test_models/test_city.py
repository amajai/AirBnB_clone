import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """Test cases for this model"""
    def test_default_values(self):
        """ Ensure that default attribute values are empty strings """
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

if __name__ == '__main__':
    unittest.main()
