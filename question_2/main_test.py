import unittest
from question_2.main import filter_names


class TestFilterNames(unittest.TestCase):

    def setUp(self):
        self.clients = [
            {"id": 1, "first_name": "John", "last_name": "Doe"},
            {"id": 2, "first_name": "Jane", "last_name": "Smith"},
            {"id": 3, "first_name": "Mark", "last_name": "Johnson"},
            {"id": 4, "first_name": "Anna", "last_name": "Brown"},
            {"id": 4, "first_name": "Michael", "last_name": "Johnson"},
        ]

    def test_filter_names(self):
        filtered_clients = filter_names(self.clients)

        expected_result = [
            {"id": 1, "first_name": "John", "last_name": "Doe"},
            {"id": 4, "first_name": "Anna", "last_name": "Brown"},
            {"id": 2, "first_name": "Jane", "last_name": "Smith"},
            {"id": 3, "first_name": "Mark", "last_name": "Johnson"},
        ]

        self.assertEqual(filtered_clients, expected_result)


if __name__ == '__main__':
    unittest.main()
