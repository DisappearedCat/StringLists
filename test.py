import unittest, main


class Test(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(main.is_palindrome('aa'))
        self.assertTrue(main.is_palindrome('a'))
        self.assertTrue(main.is_palindrome('abba'))
        self.assertTrue(main.is_palindrome('abccba'))
        self.assertTrue(main.is_palindrome('level'))
        self.assertTrue(main.is_palindrome('Noon'))
        self.assertFalse(main.is_palindrome('ab'))
        self.assertFalse(main.is_palindrome('abccbb'))
        self.assertFalse(main.is_palindrome('Wolf'))
        self.assertFalse(main.is_palindrome('Pen'))
        self.assertFalse(main.is_palindrome('lantern'))


if __name__ == '__main__':
    unittest.main()
