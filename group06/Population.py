import group06.Genome as gn
import numpy as np


class Population:
    # crea la poblacion inicial
    def __init__(self, popSize, genSize, fitnes, min, max):
        self.popSize = popSize
        self.genSize = genSize
        self.fitnes = fitnes
        self.min = min
        self.max = max
        i = 0
        self.list = []
        while i < self.popSize:
            var = np.random.uniform(min, max, genSize)
            list.append(gn(var, fitnes(var)))
        pass

    def __init__(self):
        self.list = []
        pass

    def getGenome(self, intdex):
        pass

    def add(self, genome):
        pass

    def remove(self, index, genome):
        pass

    def ascOrdered(self, fitnes):
        pass

    def desOrdered(self):
        pass

    pass
