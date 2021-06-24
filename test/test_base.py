import sys
sys.path.append("../")
sys.path.append("./")

from open_pdf.image import Image
from open_pdf.pdf import PDF

class TestBase:
    def __init__(self) -> None:

        output = "" #Output DIR

        self._image = Image(output)
        self._pdf = PDF(output)

        self._result = None

        self._multiple_pdf = [
            #Path
        ]

        self._single_pdf = [
            #Path
        ]


        self._multiple_images = [
            #Path            
        ]

        self._single_image = [
            #Path
        ]