import unittest
from spellcheck import SpellChecker
class TestSpellChecker(unittest.TestCase):

    def setUp(self):
        self.spellChecker = SpellChecker()
        self.spellChecker.load_words('spell.words')

    def test_spell_checker(self):
        self.assertEqual(53751, len(self.spellChecker.words))
        self.assertTrue(self.spellChecker.check_word('zygotic'))
        self.assertEqual([{'line': 1, 'pos': 9, 'word': 'mistasdas'}],
                self.spellChecker.check_words('zygotic mistasdas elementary'))
        self.assertEqual([],self.spellChecker.check_words('our first correct sentence'))
        self.assertEqual(0,len(self.spellChecker.check_words('Our first correct sentence.')))
        self.assertEqual([{'line': 1, 'pos': 9, 'word': 'mistasdas'}, {'line': 1, 'pos': 19, 'word': 'spelllleeeing'}],
                self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary'))
        self.assertEqual(2,len(self.spellChecker.check_words('zygotic mistasdas spelllleeeing elementary')))
        self.assertEqual(0, len(self.spellChecker.check_document("karen.txt")))
        #self.assertEqual(0, len(self.spellChecker.check_document('spell.words')))
        self.assertEqual(26, len(self.spellChecker.check_dir("/Users/karenbyrne/Desktop/python_files/")))
        self.assertEqual(2, len(self.spellChecker.check_dir("/Users/karenbyrne/Desktop/python_files/")))
        #spellChecker.check_document(file)
  
if __name__ == '__main__':
    unittest.main()