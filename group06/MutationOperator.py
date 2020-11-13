import abc
from abc import ABC


class MutationOperator(ABC):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def apply(self, genomes):
        pass

    pass
