from .Population import Population as Population
from .operadores.CurrentToRand import CurrentToRand as Mutation
from .operadores.Arithmetic import Arithmetic as Crossover
from .operadores.Uniform import Uniforme as Selection
from .operadores.Elitist import Elitist as Replacement


class EA(object):
    def __init__(self, f_fitnes, bounds, population):
        self.population = population
        self.nVar = len(bounds)
        self.min = bounds[0][0]
        self.max = bounds[0][1]
        self.f_fitnes = f_fitnes
        pass



    def run(self, iteraciones):
        i = 0

        popu = pop.Population(self.population, self.fitnes, self.min, self.max)  # conseguimos la poblacion inicial
        while i < iteraciones:
            newGen = pop.Population()
            j = 0
            while j < self.population:
                target = popu.getGenome(j)
                donor1 = popu.getGenome(0)
                donor2 = popu.getGenome(self.population / 2)
                donor3 = popu.getGenome(self.population - 1)
                mutation = mut.MutationOperator.apply([target, donor1, donor2, donor3])
                trial = cro.CrossoverOperator.apply([target, mutation])
                if target.getFitnes() <= trial.getFitnes():
                    newGen.add(target)
                    pass
                else:
                    newGen.add(trial)
                    pass
                j += 1
                pass
            popu = newGen
            i += 1
            pass
        pass

    def best(self):

        pass
