
from abc import ABC


class CrossoverOperator(ABC):
    __metaclass__ = ABC.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def apply(self, genomes):
        pass

    pass
