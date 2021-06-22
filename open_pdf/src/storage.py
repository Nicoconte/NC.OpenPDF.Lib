import os
from uuid import uuid4

class Storage:
    def __init__(self, output_dir):
        self._output_dir = output_dir
        self._filename = ""

    def _exists(self, name: str) -> bool:
        files = os.listdir(self._output_dir)
        return name in files

    def _rename_file(self, name: str) -> str:
        return f"{name.split('.pdf')[0]}_{uuid4()}.pdf"       