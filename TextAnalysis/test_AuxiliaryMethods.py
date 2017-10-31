import unittest
import PYModules.AuxiliaryMethods as Aux

#print(Aux.checkAnalysisText("   "))

class AuxiliaryMethodsTest(unittest.TestCase):
    def test_checkAnalysisText(self):
        self.assertEqual(Aux.checkAnalysisText("   "), False)
        self.assertEqual(Aux.checkAnalysisText("                    "), False)
        self.assertEqual(Aux.checkAnalysisText(123), False)
        self.assertEqual(Aux.checkAnalysisText([1,2,3,4]), False)
        self.assertEqual(Aux.checkAnalysisText("1231"), True)
        self.assertEqual(Aux.checkAnalysisText("    Hello World!!!      "), True)

    def test_getWordsFromString(self):
        self.assertIsInstance(Aux.getWordsFromString("Hello world"),dict)
        self.assertEqual(Aux.getWordsFromString(""), {})

    def test_analysisText(self):
        self.assertIsInstance(Aux.analysisText("    Hello World!!!      "),tuple)
        self.assertIsInstance(Aux.analysisText(""), tuple)


if __name__ == '__main__':
    unittest.main()