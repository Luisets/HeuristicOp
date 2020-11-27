from ..MutationOperator import MutationOperator
from ..Genome import Genome as Genome

class CurrentToRand(MutationOperator):

    def __init__(self, f_fitnes):
        self.f_fitnes = f_fitnes
        self.F = 0.8
        pass
    
    def apply(self, genomes):
        x_i = genomes[0].getSolution()
        v_1 = genomes[1].getSolution()
        v_2 = genomes[2].getSolution()
        v_3 = genomes[3].getSolution()
        mutant = x_i + self.F * (v_1 - x_i) + self.F * (v_2 - v_3)
        return Genome(mutant, self.f_fitnes(mutant))
        pass

    pass
