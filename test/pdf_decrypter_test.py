import unittest

from test_base import TestBase

class PDFDecrypterTest(unittest.TestCase, TestBase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        TestBase.__init__(self)

    def test_decrypt_single_pdf(self):
        self._result = self._pdf.decrypt(
            self._single_pdf[0],
            "123",
            "Owo_inseguro.pdf"
        )

        self.assertEqual(self._result, True)

if __name__ == "__main__":
    unittest.main()