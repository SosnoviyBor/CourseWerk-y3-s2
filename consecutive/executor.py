import os
import time
import pickle

from utils.generator import generate_regular_matrices
from utils.consts import *
from utils.results import *
from .matrix import Matrix

def do_the_thing(write_to_file:bool) -> None:
    if not DEBUG_MODE:
        results = []
        # iterate over files in directory
        for filename in os.listdir(MATRICES_DIR):
            filepath = os.path.join(MATRICES_DIR, filename)
            with open(filepath, "rb") as file:
                # matrices list is loaded!
                all_matrices = pickle.load(file)
                
                time_start = time.time()    # in seconds
                for matrix in all_matrices:
                    Matrix(matrix).inverse()
                time_elapsed = time.time() - time_start
                
                d = len(all_matrices[0])    # matrices dimentions
                c = len(all_matrices)       # matrices count
                results.append(Result(d,c,time_elapsed))    # save the results
                print(f"C | Successfeully inversed d-{d} c-{c} in {time_elapsed = }")
        # write results to excel
        results.sort()
        if write_to_file:
            write_results(results, "consecutive")
    else:
        inp = [3, 1]
        # generate single simple matrix for debugging purposes
        better_matrix = Matrix(generate_regular_matrices(*inp)[0])
        print("C | Initial matrix")
        better_matrix.print()
        
        better_matrix.inverse()
        print("\nC | Inversed matrix")
        better_matrix.print()