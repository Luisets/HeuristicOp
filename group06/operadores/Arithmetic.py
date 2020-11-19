from ..MutationOperator import CrossoverOperator


class Arithmetic(CrossoverOperator):
    CR = 0.5

    def apply(self, genomes):
        return (genomes[0] + genomes[1]) / 2
        pass

    pass
