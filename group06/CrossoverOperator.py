import zope.interface
class CrossoverOperator(zope.Interface):
    def apply(self, genomes):
        return (genomes[0] + genomes[1])/2
        pass
    pass
