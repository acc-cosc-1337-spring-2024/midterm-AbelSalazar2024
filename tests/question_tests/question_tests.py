import unittest

from src.question_a.question_a import get_fahrenheit
from src.question_b.question_b import is_prime
from src.question_c.question_c import sum_even 
from src.question_d.question_d import reverse_string


class Test_Config(unittest.TestCase):

    def test_get_fahrenheit(self):
        self.assertEqual(get_fahrenheit(0), 32)
        self.assertEqual(get_fahrenheit(5), 41)
        self.assertEqual(get_fahrenheit(10), 50)

    def test_is_prime(self):
        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(11), True)

    def test_sum_even(self):
        self.assertEqual(30, sum_even(11))
        self.assertEqual(30, sum_even(10))
        self.assertEqual(20, sum_even(8))      

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        self.assertEqual(reverse_string("hello"), "olleh")




        
