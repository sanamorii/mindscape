
from dataclasses import dataclass

@dataclass()
class Note:
    path: str = None

class Vault:
    def __init__(self):
        self.root : str
        self.notes : dict[str, Note] = {}

    def scan(self):
        raise NotImplementedError()