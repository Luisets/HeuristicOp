import group06.Genome as gp
class MutationOperator:
    def apply(self, genomes):
        # completar con F
        mutant = genomes[0].getGenome() + (genomes[3].getGenome - genomes[0].getGenome) + (genomes[1].getGenome - genomes[2].getGenome)
        return mutant
    pass