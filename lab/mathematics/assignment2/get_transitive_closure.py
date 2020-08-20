import matplotlib.pyplot as plt
import numpy
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
    out_text = "Transitive closure using Warshall’s algorithm"
    start_1 = datetime.datetime.now()
    transitive_matrix: list
    if algorithm == 'Warshall’s':
        transitive_matrix = warshall_transitive_closure(input_matrix, n)
    else:
        transitive_matrix = naive_transitive_closure(input_matrix, n)

    time_taken_1 = datetime.datetime.now() - start_1
    timeTaken = (time_taken_1.total_seconds() * 1000 +
                 time_taken_1.microseconds) / 1000
    return timeTaken, transitive_matrix


'''
apply warshall transitive closure to matrix
'''


def warshall_transitive_closure(input_matrix, n):
    output_met = [i[:]for i in input_matrix]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                output_met[i][j] = output_met[i][j] or(
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
                output_met[k][i] = input_met1[k][i] or input_met2[k][i] or output_met[k][i] or(
                    input_met1[k][j] and input_met2[j][i])
    return output_met


'''
plot graph
'''


def plot_graph(x, warshallTimeTaken, naiveTimeTaken):
    plt.rcParams["figure.figsize"] = (20, 8)
    # plotting the first plot
    plt.plot(x, warshallTimeTaken, label="Warshall's")
    # Declaring the points for second line plot
    # plotting the second plot
    plt.plot(x, naiveTimeTaken, label="Naive's")

    # Labeling the X-axis
    plt.xlabel('Order of matrix')
    # Labeling the Y-axis
    plt.ylabel('Execution time taken(milliseconds)')
    # Give a title to the graph
    plt.title('Warshall’s & Naive’s Execution Time vs Matrix Size')

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
    range_1 = 15
    f = open(getfolderPath() + "\\output.txt", "a")
    for p in range(range_1):
        n = n_start + p
        x.append(n)
        input_matrix = generate_matrix(n, rel_waight)
        print("Matrix : ", n - 9, " of order ", n, "x", n,  file=f)
        print("Random Generated Input Matrix", file=f)
        print_matrix(input_matrix, n, f)
        out_text = "Transitive closure using Warshall’s algorithm"
        warshall_result = find_transitive_closure(input_matrix, n,"Warshall’s")
        warshallTimeTaken.append(warshall_result[0])       
        out_text = "Transitive closure using Naive’s algorithm"
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
