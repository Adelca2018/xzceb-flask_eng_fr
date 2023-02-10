import unittest  # package for testing functions

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase): 
    def test_french_to_english(self): 
        self.assertEqual(french_to_english(None),None ) # test for null input.
        self.assertEqual(french_to_english("Bonjour"), "Hello")  # test bonjour translated to hello
        

    def test_english_to_french(self): 
        self.assertEqual(english_to_french(None), None) # test for null input
        self.assertEqual(english_to_french("Hello"), "Bonjour") # test Hello translated to Bonjour
        
unittest.main()