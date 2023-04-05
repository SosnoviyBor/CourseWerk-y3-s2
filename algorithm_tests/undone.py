from fractions import Fraction
from typing import List
import multiprocessing as mp
import time

class Matrix:
    def __init__(self, matrix:List[List[int|float]]) -> None:
        self.input_matrix = matrix
        self.size = len(matrix)
        self.ident_matrix = self.create_identity_matrix()

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
    
    # Gauss elimination + LU decomposition
    def inverse(self, is_floats:bool) -> List[List[int|float]]:
        # pool = mp.Pool()
        for i in range(self.size):
            scale = self.input_matrix[i][i]
            
            for col in range(self.size):
                if i != col:
                    self.input_matrix[i][col] = self.input_matrix[i][col] / scale
                    self.ident_matrix[i][col] = self.ident_matrix[i][col] / scale
            
            if i > self.size:
                for row in range(i+1):
                    factor = self.input_matrix[row][i]
                    for col in range(self.size):
                        self.input_matrix[row][col] -= factor * self.input_matrix[i][col]
                        self.ident_matrix[row][col] -= factor * self.input_matrix[i][col]
        
        print("     A mat")
        self.print(self.input_matrix)
        print("     B mat")
        self.print(self.ident_matrix)
        
        for zeroingCol in range(self.size, 1):
            for row in range(zeroingCol-1, 0):
                factor = self.input_matrix[row][zeroingCol]
                for col in range(self.size):
                    self.input_matrix[row][col] -= factor * self.input_matrix[zeroingCol][col]
                    self.ident_matrix[row][col] -= factor * self.input_matrix[zeroingCol][col]
            
        return self.ident_matrix