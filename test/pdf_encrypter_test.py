import unittest

from test_base import TestBase

class PDFEncrypterTest(unittest.TestCase, TestBase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        TestBase.__init__(self)

    def test_encrypt_single_pdf(self):
        self._result = self._pdf.encrypt(
            self._single_pdf[0],
            "123",
            "Owo_seguro.pdf"
        )

        self.assertEqual(self._result, True)

if __name__ == "__main__":
    unittest.main()