import numpy as np


def f(x):
    return 1/x
    pass
def main():
    tupla = np.array([1, 4, 3, 6, 2])
    tupla = np.append(tupla[1:5], [9, 5])
    lista = [2, 5, 8, 1, 3]
    lista.insert(0, 7)
    lista.sort(key = f)
    
    print(lista)
    pass

if __name__ == "__main__":
    main()
    pass

