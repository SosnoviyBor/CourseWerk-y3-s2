import os
import time
import pickle
import openpyxl as xl

from utils.generator import generate_regular_matrices
from utils.consts import *
from .matrix import Matrix

def do_the_thing() -> None:
    if not DEBUG_MODE:
        # iterate over files in directory
        for filename in os.listdir(MATRICES_DIR):
            filepath = os.path.join(MATRICES_DIR, filename)
            with open(filepath, "rb") as file:
                # matrices list is loaded!
                all_matrices = pickle.load(file)
                # TODO here
                # start time
                for matrix in all_matrices:
                    Matrix(matrix).inverse()
                
                d = len(all_matrices[0])
                c = len(all_matrices)
                # end time
                # write results to excel
                print(f"C | Successfeully inversed d-{d} c-{c}")
    else:
        inp = [3, 1]
        # generate single simple matrix for debugging purposes
        better_matrix = Matrix(generate_regular_matrices(*inp)[0])
        print("C | Initial matrix")
        better_matrix.print()
        
        better_matrix.inverse()
        print("\nC | Inversed matrix")
        better_matrix.print()