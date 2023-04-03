from typing import List

import pickle
import numpy as np

def generate_regular_matrices(dim:int, amount:int) -> List[List[float]]:
    """Generates square matrixes with float values

    Args:
        dim (int): matrix dimention,
        amount (int): amount of matrixes generated
    
    Returns:
        List[List[float]]: list of matrices
    """
    matrices = []
    for _ in range(amount):
        # took it from
        # https://stackoverflow.com/questions/73426718/generating-invertible-matrices-in-numpy-tensorflow
        matrix = np.random.rand(dim, dim)
        max_main_axis_vals = np.sum(np.abs(matrix), axis=1)
        np.fill_diagonal(matrix, max_main_axis_vals)
        matrices.append(matrix.tolist())
    return matrices

# generate initial data
if __name__ == "__main__":
    creation_data = [
        [1000, 30],
    ]
    
    for params in creation_data:
        dim = params[0]
        count = params[1]
        matrices = generate_regular_matrices(*params)
        with open(f"matrices/matrices d-{dim} c-{count}", "wb") as file:
            pickle.dump(matrices, file)
            print(f"Generated {count} matrices with dim {dim}")