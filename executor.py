import os
import time
import pickle

from utils.consts import MATRICES_DIR
from utils.result_manager import Result, write_results
import algorithms

def do_the_thing(sync:bool, write_to_file:bool, debug_mode:bool) -> None:
    # message thingy
    if sync:
        mode = "Sync"
    else:
        mode = "Mult"

    if not debug_mode:
        results = []
        # iterate over files in directory
        for filename in os.listdir(MATRICES_DIR):
            filepath = os.path.join(MATRICES_DIR, filename)
            with open(filepath, "rb") as file:
                # matrices list is loaded!
                all_matrices = pickle.load(file)
                d = len(all_matrices[0])    # matrices dimentions
                c = len(all_matrices)       # matrices count
                
                print(f"{mode} | Starting the inversion of d-{d} c-{c}")
                time_start = time.perf_counter()    # in seconds
                for matrix in all_matrices:
                    if sync: algorithms.synchronous.Matrix(matrix).inverse(is_floats=True)
                    else: algorithms.multiprocessed.Matrix(matrix).inverse(is_floats=True)
                time_elapsed = time.perf_counter() - time_start
                
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
            processor = algorithms.synchronous.Matrix(inp)
        else:
            processor = algorithms.multiprocessed.Matrix(inp)

        print(f"{mode} | Initial matrix")
        processor.print(processor.inp_matrix)
        
        result = processor.inverse(is_floats=False)
        print(f"{mode} | Inversed matrix")
        processor.print(result)

if __name__ == "__main__":
    # handy shortcut
    do_the_thing(sync=False,
                 write_to_file=False,
                 debug_mode=True)