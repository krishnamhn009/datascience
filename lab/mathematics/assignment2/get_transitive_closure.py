import matplotlib.pyplot as plt
import numpy as np
import random
import datetime


'''
creates random matrices of order 10 to 100, with values 0 or 1.
'''


def generate_matrix(n, rel_waight):
    list1 = [0, 1]
    matrix = [random.choices(list1, weights=(
        100 - rel_waight, rel_waight), k=n) for x in range(n)]
    return matrix


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


def find_transitive_closure(input_matrix, n, algorithm='Warshall’s'):
    start = datetime.datetime.now()
    transitive_matrix: list
    if algorithm == 'Warshall’s':
        transitive_matrix = warshall_transitive_closure(input_matrix, n)
    else:
        transitive_matrix = naive_transitive_closure(input_matrix, n)
    end_2 = datetime.datetime.now()
    timeTaken = end_2 - start
    timeTakenMilliseconds = (timeTaken.total_seconds() * 1000 +
                             timeTaken.microseconds / 1000)
    return timeTakenMilliseconds, transitive_matrix


'''
apply warshall transitive closure to matrix
'''


def warshall_transitive_closure(input_matrix, n):
    output_met = [i[:] for i in input_matrix]
    '''output_met[][] will be the output matrix that will finally
        have reachability values.
        Initialize the solution matrix same as input graph matrix'''

    '''Add all vertices one by one to the set of intermediate
        vertices.
         ---> Before start of a iteration, we have reachability value
         for all pairs of vertices such that the reachability values
          consider only the vertices in set
        {0, 1, 2, .. k-1} as intermediate vertices.
          ----> After the end of an iteration, vertex no. k is
         added to the set of intermediate vertices and the
        set becomes {0, 1, 2, .. k}'''
    for k in range(n):
        for i in range(n):
            for j in range(n):
                output_met[i][j] = output_met[i][j] or (
                    output_met[i][k] and output_met[k][j])
    return output_met


'''
naive transititve closure algorithm 
'''


def naive_transitive_closure(input_matrix, n):
    a = input_matrix
    b = mat_mult(a, a, n)
    for k in range(n - 1):
        b = mat_mult(b, a, n)
    output_met = b
    return output_met


'''

'''


def mat_mult(input_met1, input_met2, n):
    output_met = [i[:]for i in input_met1]
    for k in range(n):
        for i in range(n):
            output_met[k][i] = 0
            for j in range(n):
                output_met[k][i] = input_met1[k][i] or input_met2[k][i] or output_met[k][i] or (
                    input_met1[k][j] and input_met2[j][i])
    return output_met


'''
plot log log graph
'''


def plot_graph(x, warshallTimeTaken, naiveTimeTaken):
    plt.rcParams["figure.figsize"] = (20, 8)
    plt.plot()
    plt.loglog(x, warshallTimeTaken, label="Warshall's")
    plt.loglog(x, naiveTimeTaken, label="Naive's")
    # Labeling the X-axis
    plt.xlabel('Matrix Size', fontsize=12)
    # Labeling the Y-axis
    plt.ylabel('Execution time taken(milliseconds)', fontsize=16)
    # Give a title to the graph
    plt.title('Warshall’s & Naive’s Execution Time vs Matrix Size')
    plt.gcf().autofmt_xdate()
    # Show a legend on the plot
    plt.legend()
    plt.show()


'''
Entry function
'''


def main():
    x = []
    warshallTimeTaken = []
    naiveTimeTaken = []
    rel_waight = 3
    n_start = 10
    range_1 = 91
    f = open(getfolderPath() + "\\output.txt", "a")
    for p in range(range_1):
        n = n_start + p
        x.append(n)
        input_matrix = generate_matrix(n, rel_waight)
        print("Matrix : ", n - 9, " of order ", n, "x", n,  file=f)
        print("Random Generated Input Matrix", file=f)
        print_matrix(input_matrix, n, f)
        warshall_result = find_transitive_closure(
            input_matrix, n, "Warshall’s")
        warshallTimeTaken.append(warshall_result[0])
        naive_result = find_transitive_closure(input_matrix, n, "Naive's")
        naiveTimeTaken.append(naive_result[0])
        print("Warshall’s algorithm - Transitive closure", file=f)
        print_matrix(warshall_result[1], n, f)
        print("Naive’s algorithm - Transitive closure", file=f)
        print_matrix(naive_result[1], n, f)
        print('Warshall’s Output Matrix and Naive’s Output Matrix Match :- ',
              warshall_result[1] == naive_result[1], file=f)  # plot

    plot_graph(x, warshallTimeTaken, naiveTimeTaken)


if __name__ == '__main__':
    main()
