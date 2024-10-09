import unittest
from src.meditation_agent import generate_meditation_script

class TestMeditationAgent(unittest.TestCase):

    def test_generate_valid_script(self):
        prompt = "Create a 60-second mindfulness meditation focused on relaxation."
        script = generate_meditation_script(prompt)
        
        self.assertIsNotNone(script)
        self.assertEqual(script.duration, 60000)
        self.assertEqual(script.focus_area, "relaxation")
        self.assertGreater(len(script.phrases), 0)

    def test_generate_invalid_script(self):
        # This test case is for invalid inputs
        prompt = ""
        script = generate_meditation_script(prompt)

        # Expect the function to return None for an invalid prompt
        self.assertIsNone(script)

if __name__ == "__main__":
    unittest.main()

