from ..ReplacementOperator import ReplacementOperator
from ..Population import Population

class Elitist(ReplacementOperator):

    def apply(self, currentGen, trialGen):
        newGen = Population(currentGen.f_fitnes, currentGen.getSize())
        for i in range(0, currentGen.getSize()):
            if currentGen.getGenome(i).getFitnes() < trialGen.getGenome(i).getFitnes():
                newGen.add(currentGen.getGenome(i))
                pass
            else:
                newGen.add(trialGen.getGenome(i))
                pass
            pass
        return newGen
        pass
    pass
