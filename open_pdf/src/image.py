from PIL import Image as PillowImage

from .storage import Storage

class Image(Storage):
    def __init__(self, output_dir):
        Storage.__init__(self, output_dir)
        self.__current_images: list = []

    def __save(self, images:list, name:str) -> bool:
        return images[0].save(f"{self._output_dir}/{name}", save_all=True, append_images=images[1:len(images)])    

    def convert_to_pdf(self, images: list, name: str="Convertido_por_OpenPDF.pdf") -> bool:

        self._filename = name

        try:
            for image in images:
                self.__current_images.append(PillowImage.open(image).convert("RGB"))

            if self._exists(self._filename):
                self._filename = self._rename_file(self._filename) 

            self.__save(self.__current_images, f"{self._filename}")

            return self._exists(self._filename)

        except Exception as e:
            print(f"Cannot convert image -> {str(e)}")