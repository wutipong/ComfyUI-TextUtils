import textutils
import unittest

class TestTextUtils(unittest.TestCase):
    def test_positive_tokens(self):
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing", "/", 0), "")
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing", "/", 1), "hello")
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing", "/", 2), "hello/world")

        
    def test_negative_tokens(self):
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing", "/", -1), "doing")
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing", "/", -2), "you/doing")

    def test_n_exceed_length(self):
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing", "/", 8), "hello/world/how/are/you/doing")
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing", "/", -6), "hello/world/how/are/you/doing")

    def test_delim_at_the_begining(self):
        self.assertEqual(textutils.create_n_token_string("/hello/world/how/are/you/doing/", "/", 0), "")
        self.assertEqual(textutils.create_n_token_string("/hello/world/how/are/you/doing/", "/", 1), "")
        self.assertEqual(textutils.create_n_token_string("/hello/world/how/are/you/doing/", "/", 2), "/hello")

    def test_delim_at_the_end(self):
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing/", "/", -1), "")
        self.assertEqual(textutils.create_n_token_string("hello/world/how/are/you/doing/", "/", -2), "doing/")

if __name__ == '__main__':
    unittest.main()