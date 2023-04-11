from fractions import Fraction
from typing import List, Any
from copy import deepcopy
import multiprocessing as mp

from utils.progress_bar import print_progress_bar

class Matrix:
    def __init__(self, matrix:List[List[int|float]]) -> None:
        self.inp_matrix = matrix
        self.size = len(self.inp_matrix)
        
        # progressbar data
        # this is NOT complexity
        # n for determinant
        # n^2 for calculating adjugate matrix
        # not counting n^2 for transponation for accuracy reasons
        # no counting n^2 for inversed matrix division since its too fast
        self.pb_total_iters = self.size + self.size**2

    def print(self, matrix:List[List[Any]]) -> None:
        """Handy method to print the matrix to the console

        Args:
            matrix (List[List[Any]]): Any 2d array
        """
        for row in matrix:
            for val in row:
                print(val, end=" ")
            print('')

    def pb_shortcut(self, pb_current_iter:int):
        """Simple shortcut for displaying the progress bar"""
        # and no, i am not bothered enough to fix its stutter here
        # i want to have a life too, you know
        print_progress_bar(iteration=pb_current_iter,
                           total=self.pb_total_iters,
                           prefix=f"Mult | Progress on d-{self.size}",
                           suffix="Complete",
                           length=50)

    def inverse(self, is_floats:bool) -> List[List[int|float]]:
        """Inverse the inputed matrix

        Args:
            is_floats (bool): is data in matrix type of float or int

        Returns:
            List[List[int|float]]: inversed matrix
        """
        pb_current_iter = 0
        self.pb_shortcut(pb_current_iter)
        # check if matrix is square-like
        if self.size != len(self.inp_matrix[0]):
            raise Exception("Input matrix must have same dimentions on both axis'")
        
        # get matrix determinant
        pool1 = mp.Pool()
        pb_current_iter += 1
        det = self.matrix_determinant(pool1, pb_current_iter)

        # calculate minor matrix
        # left to right, top to bottom
        pool2 = mp.Pool()
        manager = mp.Manager()
        minor_matrix_data = manager.list([])
        args = []
        for i in range(self.size):
            for j in range(self.size):
                pb_current_iter += 1
                args.append((self.inp_matrix, i, j, pb_current_iter, minor_matrix_data))
        pool2.map(self.minor, args)

        # prepare empty minor matrix for next step
        minor_matrix = [[None for _ in range(self.size)] for _ in range(self.size)]

        # parse processes' results
        pool2.close()
        pool2.join()

        for data in minor_matrix_data:
            val = data[0]
            true_row = data[1]
            true_col = data[2]
            minor_matrix[true_row][true_col] = val

        # transpose minor matrix
        adjugate_matrix = self.transpose(minor_matrix)

        pool1.close()
        pool1.join()
        
        # divide adjugate matrix
        # left to right, top to bottom
        for row in range(self.size):
            for col in range(self.size):
                if is_floats:
                    adjugate_matrix[row][col] = adjugate_matrix[row][col] / det
                else:
                    adjugate_matrix[row][col] = Fraction(adjugate_matrix[row][col], det)
        
        # since progressbars like to screw up in multithreading
        # for some completely inknown reason...
        self.pb_shortcut(self.pb_total_iters)
        return adjugate_matrix

    def matrix_determinant(self, pool:mp.Pool, pb_current_iter:int) -> int|float:
        """Calculate matrix determinant

        Returns:
            int|float: determinant value
        """
        manager = mp.Manager()
        
        col = 0
        results = manager.list([])
        args = []
        for row in range(self.size):
            args.append((self.inp_matrix, row, col, pb_current_iter, results))
        pool.map(self.minor, args)
        
        det = 0
        for data in results:
            minor, row, col = data
            det += minor * self.inp_matrix[row][col]
        
        if det == 0:
            raise Exception("Matrix' determinant = 0. This matrix does not have inverse variant")
        
        return det

    def minor(self, args:tuple) -> int|float:
        """Calculate minor of given coordinates

        Args:
            matrix (List[List[int | float]]): matrix to get the minor from
            main_row (int): x coordinate
            main_col (int): y coordinate

        Returns:
            int|float: minor value
        """
        matrix, main_row, main_col, pb_current_iter, minor_matrix_data = args
        mini_matrix = deepcopy(matrix)
        
        # drop x row and y column
        row = 0
        criteria = self.size
        while row < criteria:
            del mini_matrix[row][main_col]
            if row == main_row:
                del mini_matrix[row]
                criteria -= 1
            row += 1
        # час костилів настав!
        if main_row != self.size-1:
            del mini_matrix[main_row][main_col]
        size = len(mini_matrix)
        
        det = 0
        
        # iterate positively
        col = 0
        for _ in range(size):
            row = 0
            col += 1
            local_det = 1
            for _ in range(size):
                # column wrap
                if col >= size:
                    col -= size
                
                local_det *= mini_matrix[row][col]
                
                row += 1
                col += 1
            det += local_det
        
        # iterate negatively
        col = size-1
        for _ in range(size):
            row = 0
            col -= 1
            local_det = 1
            for _ in range(size):
                # column wrap
                if col < 0:
                    col += size

                local_det *= mini_matrix[row][col]
                
                row += 1
                col -= 1
            det -= local_det
        
        det *= (-1) ** (main_row + main_col)
        
        self.pb_shortcut(pb_current_iter)
        
        minor_matrix_data.append((det, main_row, main_col))

    def transpose(self, matrix:List[List[int|float]]) -> List[List[int|float]]:
        """Transposes matrix
        Args:
            matrix (List[List[int|float]]): any matrix
        Returns:
            List[List[int|float]]: transposed matrix
        """
        for i in range(self.size):
            for j in  range(self.size):
                if i != j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix