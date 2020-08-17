import numpy
import matplotlib.pyplot as plt
import random
import datetime


'''
get working folder path
'''


def getfolderPath():
    from inspect import currentframe, getframeinfo
    from pathlib import Path

    filename = getframeinfo(currentframe()).filename
    parent = Path(filename).resolve().parent
    return str(parent.joinpath())


'''
# print array in matrix format
'''


def print_matrix(output_matrix, n, f):
    for i in range(n):
        for j in range(n):
            print('%1d ' % (output_matrix[i][j]), end="", file=f)
        print("", file=f)


'''
naive transititve algoritham algoritham 
'''


def naive_transitive_closure(input_matrix, n):
    a = input_matrix
    b = mat_mult(a, a, n)
    for k in range(n - 1):
        b = mat_mult(b, a, n)
    output_matrix = b
    return output_matrix


'''

'''


def mat_mult(input_matrix1, input_matrix2, n):
    output_met = [i[:]for i in input_matrix1]
    for k in range(n):
        for i in range(n):
            output_met[k][i] = 0
            for j in range(n):
                output_met[k][i] = input_matrix1[k][i] or input_matrix2[k][i] or output_met[k][i] or(
                    input_matrix1[k][j] and input_matrix2[j][i])
    return output_met


'''
Entry function
'''


def main():
    x = []
    y = []
    r = []
    print("finding transitive closure of matrix")
    print("This program follow below steps: \n 1.Generate random matrox of order 10 to 100 order")
    print(" 2.Find transitive closure using Naive Algoritham & Warshall Algoritham and comapte time taken by both algoritham \n 3.Plot a graph")
    rel_waight = 3
    n_start = 10
    range_1 = 91
    print(datetime.datetime.now())
    plt.rcParams["figure.figsize"] = (20, 8)
    f = open(getfolderPath() + "\\output.txt", "a")
    for p in range(range_1):
        n = n_start + p
        x.append(n)
        input_mat = generate_matrix(n, rel_waight)
        print(input_mat)
        print("Matrix : ", n - 9, " of order ", n, "x", n, " Matrix", file=f)
        print("Random Generated Input Matrix", file=f)
        print_matrix(input_mat, n, f)
        out_text = "Output of Warshall’s algorithm - Transitive closure"
        start_1 = datetime.datetime.now()
        mat_algo_2 = warshall_transitive_closure(input_mat, n)
        end_1 = datetime.datetime.now()
        time_taken_1 = end_1 - start_1
        y.append(time_taken_1.total_seconds() * 1000 +
                 time_taken_1.microseconds / 1000)
        out_text = "Output of Naive’s algorithm - Transitive closure"
        start_2 = datetime.datetime.now()
        mat_algo_1 = naive_transitive_closure(input_mat, n)
        end_2 = datetime.datetime.now()
        time_taken_2 = end_2 - start_2
        r.append(time_taken_2.total_seconds() * 1000 +
                 time_taken_2.microseconds / 1000)
        print("Warshall’s algorithm - Transitive closure", file=f)
        print_matrix(mat_algo_1, n, f)
        print("Naive’s algorithm - Transitive closure", file=f)
        print_matrix(mat_algo_2, n, f)
        print('Warshall’s Output Matrix and Naive’s Output Matrix Match :- ',
              mat_algo_1 == mat_algo_2, file=f)  # plot

        print('***********************************************************************************************************')  # plot


'''
creates random matrices of order 10 to 100, with values 0 or 1.
'''


def generate_matrix(n, rel_waight):
    list1 = [0, 1]
    matrix = [random.choices(list1, weights=(
        100 - rel_waight, rel_waight), k=n) for x in range(n)]
    return matrix


'''
apply transitive closure to matrix
'''


def warshall_transitive_closure(input_matrix, n):
    output_matrix = [i[:]for i in input_matrix]
    assert (len(input_matrix) == len(input_matrix) for row in input_matrix)
    n = len(input_matrix)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                output_matrix[i][j] = input_matrix[i][j] or (
                    input_matrix[i][k] and input_matrix[k][j])
    return output_matrix


if __name__ == '__main__':
    main()
