from fractions import Fraction
from typing import List
import multiprocessing as mp
import time

"""
miltiprocessing
parallelized only LU matrices inversion

23.0 secs on d-500

literally 0 difference from test 1 omfg
"""

class Matrix:
    def __init__(self, matrix:List[List[int|float]]) -> None:
        self.input_matrix = matrix
        self.size = len(matrix)
        self.L = self.create_identity_matrix()

    # handy method to print the matrix to the console
    def print(self, matrix:List[List[int|float]]) -> None:
        for i in matrix:
            for j in i:
                print(j, end=" ")
            print('')

    # add the identity matrix to the original matrix from the right
    def create_identity_matrix(self) -> List[List[int]]:
        matrix = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix
    
    def inverse_LU(self, main_matrix):
        i_matrix = self.create_identity_matrix()
        for i in range(self.size):
            for j in range(self.size):
                if j != i:
                    ratio = main_matrix[j][i] / main_matrix[i][i]
                    for k in range(self.size):
                        main_matrix[j][k] -= main_matrix[i][k] * ratio
                        i_matrix[j][k] -= i_matrix[i][k] * ratio
        
        for i in range(self.size):
            ratio = main_matrix[i][i]
            for j in range(self.size):
                main_matrix[i][j] = main_matrix[i][j] / ratio
                i_matrix[i][j] = i_matrix[i][j] / ratio
        return i_matrix
    
    def decompose(self, i, is_floats):
        for j in range(self.size-1, i, -1):
            if i != j and self.input_matrix[j][i] != 0:
                if is_floats:
                    ratio = self.input_matrix[j][i] / self.input_matrix[i][i]
                else:
                    # python literally cant count wtf
                    ratio = Fraction(self.input_matrix[j][i], self.input_matrix[i][i])
                self.L[j][i] = ratio
                for k in range(self.size):
                    self.input_matrix[j][k] = self.input_matrix[j][k] - self.input_matrix[i][k] * ratio
    
    # Gauss elimination + LU decomposition
    def inverse(self, is_floats:bool) -> List[List[int|float]]:
        # multiprocessing this thing is literally counter-productive
        for i in range(self.size):
            for j in range(self.size-1, i, -1):
                if i != j and self.input_matrix[j][i] != 0:
                    if is_floats:
                        ratio = self.input_matrix[j][i] / self.input_matrix[i][i]
                    else:
                        # python literally cant count wtf
                        ratio = Fraction(self.input_matrix[j][i], self.input_matrix[i][i])
                    self.L[j][i] = ratio
                    for k in range(self.size):
                        self.input_matrix[j][k] = self.input_matrix[j][k] - self.input_matrix[i][k] * ratio
        
        # god bless this pdf file
        # http://home.cc.umanitoba.ca/~farhadi/Math2120/Inverse%20Using%20LU%20decomposition.pdf
        
        # parallizeable for fucking sure
        pool = mp.Pool()
        args = [self.L, self.input_matrix]
        results = pool.map(self.inverse_LU, args)
        
        # multiply these bastards
        final_matrix = []
        inverse_L = results[0]
        inverse_U = results[1]
        for i in range(self.size):
            row = []
            for j in range(self.size):
                val = 0
                for k in range(self.size):
                    val += inverse_U[i][k] * inverse_L[k][j]
                row.append(val)
            final_matrix.append(row)
            
        return final_matrix