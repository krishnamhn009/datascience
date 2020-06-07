import numpy as np
from numpy import linalg as LA


def getEigenValues(a):
    lam, u = LA.eig(a)
    return lam, u


def main(a):
    print("finding eigen value of matrix:\n", a)
    eValue, eVetors = getEigenValues(a)
    print("eigen value of matrix:\n", eValue)
    print("eigen vectors of matrix:\n", eVetors)


if __name__ == "__main__":
    main(np.matrix([[1, 2, 3], [6, 7, 8], [8, 6, 4]]))
