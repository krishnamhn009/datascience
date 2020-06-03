import numpy as np


def matrix_inverse(a):
    return np.linalg.inv(a)


def main(a):
    print("finding inverse of matrix")
    print("inverse is :", matrix_inverse(a))

if __name__ == "__main__":
    main(np.matrix([[1, 3, 7], [2, 8, 3], [7, 8, 1]]))

