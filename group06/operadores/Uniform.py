from ..SelectionOperator import SelectionOperator
from ..Genome import Genome
import numpy as np

class Uniform(SelectionOperator):

    def __init__(self):
        
        pass
    

    def apply(self, population, i):
        selection = [population.getGenome(i)]
        while len(selection) < 4:
            rand = np.random.randint(population.getSize())
            if rand != i:
                selection.append(population.getGenome(rand))
            pass
        pass
        return selection
    pass
