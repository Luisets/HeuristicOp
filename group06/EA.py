from .Population import Population as Population
from .Genome import Genome as Genome
from .operadores.CurrentToRand import CurrentToRand as Mutation
from .operadores.Arithmetic import Arithmetic as Crossover
from .operadores.Uniform import Uniform as Selection
from .operadores.Elitist import Elitist as Replacement
import numpy as np


class EA(object):
    def __init__(self, f_fitnes, bounds, populationSize):
        self.populationSize = populationSize
        self.nVar = len(bounds)
        self.min = bounds[0][0]
        self.max = bounds[0][1]
        self.f_fitnes = f_fitnes
        pass



    def run(self, iteraciones):
        self.currentGen = Population(self.f_fitnes, self.populationSize)  # conseguimos la poblacion inicial
        self.initPopulation()
        print("Primera generacion")
        self.currentGen.print()
        trialGen = Population(self.f_fitnes, self.populationSize)
        selector = Selection()
        mutator = Mutation(self.f_fitnes)
        replacer = Replacement()
        crossover = Crossover(self.f_fitnes)
        for n_gen in range(0, iteraciones):
            trialGen.clear()
            for n_indiv in range(0, self.populationSize):
                selection = selector.apply(self.currentGen, n_indiv)
                target = selection[0]
                mutation = self.ensureBounds(mutator.apply(selection))
                trial = crossover.apply([target, mutation])
                trialGen.add(trial)
                pass
            self.currentGen = replacer.apply(self.currentGen, trialGen)
            pass
        self.currentGen.ascOrdered()
        pass

    def ensureBounds(self, genome):
        vInBounds = []
        for value in genome.solution:
            if value < self.min:
                vInBounds.append(self.min)
                pass
            elif value > self.max:
                vInBounds.append(self.max)
                pass
            else:
                vInBounds.append(value)
                pass
            pass
        npArray = np.array(vInBounds)
        return Genome(npArray, self.f_fitnes(npArray))
        pass

    def initPopulation(self):
        for i in range(0, self.populationSize):
            solution = np.random.uniform(self.min, self.max, self.nVar)
            self.currentGen.add(Genome(solution, self.f_fitnes(solution)))
            pass
        pass
    
    def best(self):
        return  self.currentGen.getGenome(0)
        pass
