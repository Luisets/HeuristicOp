from .Genome import Genome as Genome
import numpy as np


class Population:
    # crea la poblacion inicial
    def __init__(self, f_fitnes, size):
        self.solPopulation = []
        self.size = size
        self.f_fitnes = f_fitnes

    def getGenome(self, intdex):
        pass

    def add(self, genome):
        self.solPopulation.append(genome)
        pass

    def remove(self, index):
        self.solPopulation.pop(index)
        pass

    def clear(self):
        self.solPopulation.clear()
        pass

    def ascOrdered(self):
        self.solPopulation.sort(key = getFitnes)
        pass

    def desOrdered(self):
        self.solPopulation.sort(key = getFitnes, reverse = True)
        pass

    pass

def getFitnes(genome):
    return genome.fitnes
    pass