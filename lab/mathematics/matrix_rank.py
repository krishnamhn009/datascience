import numpy as np

def matrix_rank(A):
    return np.linalg.matrix_rank(A)

	
def main(A):
	print('finding rank of matrix:\n',A)
	print('Rank of matrix is:',matrix_rank(A))
	
if __name__=='__main__':
	    main(np.matrix([[1,3,7],[2,8,3],[7,8,1]]))