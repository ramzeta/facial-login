import numpy as np

class VectorFacial:
    def __init__(self, encoding: np.ndarray):
        self.encoding = encoding

    def distancia(self, otro: 'VectorFacial') -> float:
        return np.linalg.norm(self.encoding - otro.encoding)
