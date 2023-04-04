import os
import time
import pickle

from utils.generator import generate_regular_matrices
from utils.consts import *
from utils.result_manager import *
from matrices import *

def do_the_thing(sync:bool, write_to_file:bool, debug_mode:bool) -> None:
    if not debug_mode:
        results = []
        # iterate over files in directory
        for filename in os.listdir(MATRICES_DIR):
            filepath = os.path.join(MATRICES_DIR, filename)
            with open(filepath, "rb") as file:
                # matrices list is loaded!
                all_matrices = pickle.load(file)
                
                time_start = time.perf_counter()    # in seconds
                for matrix in all_matrices:
                    if sync: synchronous.Matrix(matrix).inverse(floats=True)
                    else: multiprocessed.Matrix(matrix).inverse(floats=True)
                time_elapsed = time.perf_counter() - time_start
                
                d = len(all_matrices[0])    # matrices dimentions
                c = len(all_matrices)       # matrices count
                mode = "S" if sync else "M"
                results.append(Result(d,c,time_elapsed))
                print(f"{mode} | Successfeully inversed d-{d} c-{c} in {round(time_elapsed, 2)} second(s)")
        # write results to excel
        results.sort()
        if write_to_file:
            write_results(results, sync)
    else:
        inp = [
            [2,1,1,1],
            [1,2,1,1],
            [1,1,2,1],
            [1,1,1,2],
        ]
        # generate single simple matrix for debugging purposes
        if sync:
            processor = synchronous.Matrix(inp)
        else:
            processor = multiprocessed.Matrix(inp)
        print("C | Initial matrix")
        processor.print(processor.matrix)
        
        processor.inverse(floats=False)
        print("\nC | Inversed matrix")
        processor.print(processor.matrix)

if __name__ == "__main__":
    # handy shortcut
    do_the_thing(sync=True,
                 write_to_file=False,
                 debug_mode=True)