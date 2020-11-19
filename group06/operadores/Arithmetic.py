from ..CrossoverOperator import CrossoverOperator
from ..Genome import Genome

class Arithmetic(CrossoverOperator):

    def __init__(self, f_fitnes):
        self.K = 0.9
        self.f_fitnes = f_fitnes
        pass

    def apply(self, genomes):
        x_i = genomes[0].getSolution()
        mutant = genomes[1].getSolution()
        trial = x_i + self.K * (mutant - x_i)
        return Genome(trial, self.f_fitnes(trial))
        pass

    pass
