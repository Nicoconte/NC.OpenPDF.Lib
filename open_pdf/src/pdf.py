from PyPDF2 import PdfFileReader, PdfFileWriter

from .storage import Storage

class PDF(Storage):

    def __init__(self, output_dir):
        Storage.__init__(self, output_dir)
        self.__pdf_writer = PdfFileWriter()        

    def __save(self):
        if self._exists(self._filename):
            self._filename = self._rename_file(self._filename)

        with open(f"{self._output_dir}/{self._filename}", 'wb') as out:
            self.__pdf_writer.write(out)            

        return self._exists(self._filename)

    def merge(self, pdf_files: list, name="Convertido_por_OpenPDF.pdf") -> bool:        
        
        if len(pdf_files) < 2:
            return False

        self._filename = name
        
        try:
            for pdf in pdf_files:
                current_pdf = PdfFileReader(pdf)

                for index in range(current_pdf.getNumPages()):
                    self.__pdf_writer.addPage(current_pdf.getPage(index))    

            return self.__save()

        except Exception as e:
            print(f"Cannot merge -> {str(e)}")

    
    def encrypt(self, pdf_file: str, password: str, owner=None, name="Encriptado_por_OpenPDF.pdf") -> bool:
        self._filename = name

        current_pdf = PdfFileReader(pdf_file)
        try:
            for index in range(current_pdf.getNumPages()):
                self.__pdf_writer.addPage(current_pdf.getPage(index))
            
            self.__pdf_writer.encrypt(user_pwd=password, owner_pwd=owner, use_128bit=True)

            return self.__save()

        except Exception as e:
            print(f"Cannot encrypt {str(e)}")


