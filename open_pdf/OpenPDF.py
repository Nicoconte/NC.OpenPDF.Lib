from open_pdf.src.image import Image
from open_pdf.src.pdf import PDF

class OpenPDF(Image, PDF):
    def __init__(self, output_dir) -> None:
        self.image = Image(output_dir)
        self.pdf = PDF(output_dir)

    