import unittest

from test_base import TestBase

class TestImageConverter(unittest.TestCase, TestBase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        TestBase.__init__(self)


    def test_convertion_mulitple_images(self):
        self._result = self._image.convert_to_pdf(self._multiple_images, "uwu.pdf")
        self.assertEqual(self._result, True)

    def test_convertion_single_image(self):
        self._result = self._image.convert_to_pdf(self._single_image, "uwu.pdf")
        self.assertEqual(self._result, True)


if __name__ == "__main__":
    unittest.main()