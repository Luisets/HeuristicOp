from ..MutationOperator import MutationOperator
import random


class CurrentToRand(MutationOperator):

    def apply(self, genomes):
        # completar con F
        F = random.randint(0, 2)
        mutant = genomes[0].getGenome() + F * (genomes[3].getGenome - genomes[0].getGenome) + F * (
                    genomes[1].getGenome - genomes[2].getGenome)
        return mutant

    pass
