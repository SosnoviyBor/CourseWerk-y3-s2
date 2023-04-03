import os
import time
import pickle

from utils.generator import generate_regular_matrices
from utils.consts import *
from utils.results import *
from matrices import *

def do_the_thing(sync:bool, write_to_file:bool) -> None:
    if not DEBUG_MODE:
        results = []
        # iterate over files in directory
        for filename in os.listdir(MATRICES_DIR):
            filepath = os.path.join(MATRICES_DIR, filename)
            with open(filepath, "rb") as file:
                # matrices list is loaded!
                all_matrices = pickle.load(file)
                
                time_start = time.perf_counter()    # in seconds
                for matrix in all_matrices:
                    if sync: synchronous.Matrix(matrix).inverse()
                    else: multiprocessed.Matrix(matrix).inverse()
                time_elapsed = time.perf_counter() - time_start
                
                d = len(all_matrices[0])    # matrices dimentions
                c = len(all_matrices)       # matrices count
                mode = "S" if sync else "M"
                results.append(Result(d,c,time_elapsed))
                print(f"{mode} | Successfeully inversed d-{d} c-{c} in {round(time_elapsed, 2)} second(s)")
        # write results to excel
        results.sort()
        if write_to_file:
            mode = "synchronous" if sync else "multiprocessed"
            write_results(results, mode)
    else:
        inp = [
            [1,0,0,0],
            [0,2,0,0],
            [0,0,2,0],
            [0,0,0,2],
        ]
        # generate single simple matrix for debugging purposes
        if sync:
            better_matrix = synchronous.Matrix(inp)
        else:
            better_matrix = multiprocessed.Matrix(inp)
        print("C | Initial matrix")
        better_matrix.print()
        
        better_matrix.inverse()
        print("\nC | Inversed matrix")
        better_matrix.print()