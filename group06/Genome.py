import numpy as np
class Genome:
    
    def __init__(self, solution, fitnes):
        self.solution = solution
        self.fitnes = fitnes
        pass

    def getSolution(self):
        return self.solution
        pass

    def getFitnes(self):
        return self.fitnes
        pass

    pass