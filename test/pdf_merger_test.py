import unittest

from test_base import TestBase

class PDFMergerTest(unittest.TestCase, TestBase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        TestBase.__init__(self)

    def test_merge_multiple_pdf(self):
        self._result = self._pdf.merge(self._multiple_pdf, "owo_pdf.pdf") 
        self.assertEqual(self._result, True)

    def test_merge_single_pdf(self):
        self._result = self._pdf.merge(self._single_pdf, "awa_pdf.pdf")
        self.assertEqual(self._result, False)

if __name__ == "__main__":
    unittest.main()