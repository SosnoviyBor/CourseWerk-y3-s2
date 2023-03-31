from typing import List
import random

def matrix_gen(dim:int, a:int, b:int, amount:int) -> List[List[int]]:
    """Generates square matrixes

    Args:
        dim (int): matrix dimention,
        a (int): leftmost value,
        b (int): rigthmost value,
        amount (int): amount of matrixes generated
    
    Yields:
        List[List[int]]: matrix
    """
    for _ in range(amount):
        matrix = []
        for _ in range(dim):
            new_row = []
            for _ in range(dim):
                new_row.append(random.randint(a,b))
            matrix.append(new_row)
        yield matrix