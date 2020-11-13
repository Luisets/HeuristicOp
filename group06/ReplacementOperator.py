import abc
from abc import ABC


class ReplacementOperator(ABC):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pass

    @abc.abstractmethod
    def apply(self, poblacionGenomas1, poblacionGenomas2):
        pass

    pass
