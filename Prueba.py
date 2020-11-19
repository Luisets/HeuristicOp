from group06.EA import EA
import numpy as np

def f(x):
    return sum(x)
    pass

def main():
    mybounds = [(0, 8)] * 6
    myea = EA(f, mybounds, 50)
    myea.run(5000)
    bestSol = myea.best()
    print("ultima pob")
    myea.currentGen.print()
    print("Best Genoma:")
    print("\tSolution: {}, Fitnes: {}".format(bestSol.solution, bestSol.fitnes))
    pass

if __name__ == "__main__":
    main()
    pass

