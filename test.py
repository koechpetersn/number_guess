import unittest
from num_guess import number_guess


class TestNumGuess(unittest.TestCase):
    def test_number_guess_returns_correct_response(self):
      text1='You are a genious just like the owner of this code!'
      text2='Sorry,your guess is 3 step(s) higher from the correct number!'
      text3='Sorry,your guess is 3 step(s) behind the correct number!'
      self.assertEqual(number_guess(10,10),text1,msg='A matching guess should return True!')
      self.assertEqual(number_guess(1,1),text1,msg='A matching guess should return True!')
      self.assertEqual(number_guess(5,5),text1,msg='A matching guess should return True!')
      self.assertEqual(number_guess(2,5),text2,msg='A matching guess should return True!')
      self.assertEqual(number_guess(8,5),text3,msg='A matching guess should return True!')
if __name__ == "__main__":
    unittest.main(exit = False)
