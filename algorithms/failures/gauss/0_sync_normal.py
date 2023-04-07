from fractions import Fraction
from typing import List

class Matrix:
    def __init__(self, matrix:List[List[int|float]]) -> None:
        self.matrix = matrix
        self.order = len(self.matrix)

    # handy method to print the matrix to the console
    def print(self, matrix:List[List[int|float]]) -> None:
        for i in matrix:
            for j in i:
                print(j, end=" ")
            print('')

    # add the identity matrix to the original matrix from the right
    def create_identity_matrix(self) -> List[List[int]]:
        identity_matrix = []
        for i in range(self.order):
            row = []
            for j in range(self.order):
                if i == j:
                    row.append(1)
                else:
                    row.append(0)
            identity_matrix.append(row)
        return identity_matrix

    # invert the matrix
    def inverse(self, is_floats:bool) -> List[List[int|float]]:
        # 13.0s per d-500 matrix
        # why the fuck are you so fast????
        aug_matrix = self.create_identity_matrix()

        for i in range(self.order):     # Цей цикл розпаралелити не можна, бо будуть колізії
            for j in range(self.order): # Розпаралеливши цей цикл, швидкість падає десь у 30 разів
                if j != i:
                    if is_floats:
                        ratio = self.matrix[j][i] / self.matrix[i][i]
                    else:
                        ratio = Fraction(self.matrix[j][i], self.matrix[i][i])
                    for k in range(self.order):
                        self.matrix[j][k] -= self.matrix[i][k] * ratio
                        aug_matrix[j][k] -= aug_matrix[i][k] * ratio
        
        for i in range(self.order):
            ratio = self.matrix[i][i]
            for j in range(self.order):
                if is_floats:
                    self.matrix[i][j] = self.matrix[i][j] / ratio
                    aug_matrix[i][j] = aug_matrix[i][j] / ratio
                else:
                    self.matrix[i][j] = Fraction(self.matrix[i][j], ratio)
                    aug_matrix[i][j] = Fraction(aug_matrix[i][j], ratio)
        
        return aug_matrix