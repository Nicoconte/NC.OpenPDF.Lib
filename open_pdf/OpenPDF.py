import os
from uuid import uuid4

from PIL import Image

class OpenPDF:

    def __init__(self, output_dir="") -> None:
        self.__output_dir = output_dir
        self.__current_images: list = []

    def __save_images(self, images:list, filename:str) -> bool:
        return images[0].save(f"{self.__output_dir}/{filename}", save_all=True, append_images=images[1:len(images)])

    def __exists(self, filename: str) -> bool:
        files = os.listdir(self.__output_dir)
        return filename in files

    def set_output_dir(self, output_dir: str) -> None:
        self.__output_dir = output_dir

    def convert_img_to_pdf(self, images: list, filename: str="Convertido_por_OpenPDF.pdf") -> None:

        pdf_filename = filename

        try:
            for image in images:
                self.__current_images.append(Image.open(image).convert("RGB"))

            if self.__exists(pdf_filename):
                pdf_filename = f"{pdf_filename.split('.pdf')[0]}_{uuid4()}.pdf"

            self.__save_images(self.__current_images, f"{pdf_filename}")

            return self.__exists(pdf_filename)

        except Exception as e:
            print(f"Cannot convert image -> {str(e)}")



    