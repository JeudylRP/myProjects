import unittest
from meditation_assistant import get_meditation_suggestion

class TestMeditationAssistant(unittest.TestCase):

    def test_get_meditation_suggestion(self):
        user_input = "I feel stressed."
        result = get_meditation_suggestion(user_input)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_get_meditation_suggestion_empty_input(self):
        user_input = ""
        result = get_meditation_suggestion(user_input)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

    def test_get_meditation_suggestion_special_characters(self):
        user_input = "@#$%^&*"
        result = get_meditation_suggestion(user_input)
        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()
