from typing import List
import generator

def invert(matrix:List[List[int]]) -> List[List[int]] | None:
    """Inverts given matrix

    Args:
        matrix (List[List[int]]): Any square matrix

    Returns:
        List[List[int]] | None: inversed matrix if exists
    """
    dim = len(matrix)
    # check if matrix is square-like
    if dim != len(matrix[0]):
        return None
    
    # get matrix determinant
    det = matrix_determinant(matrix,dim)
    if det == 0:
        return None
    
    inverted_matrix = []
    # left to right, top to bottom
    # calculate the inversed matrix
    for i in range(dim):
        row = []
        for j in range(dim):
            val = minor(matrix, dim, j, i) / det
            row.append(val)
        inverted_matrix.append(row)
    inverted_matrix = transpose(inverted_matrix, dim)
    return inverted_matrix

class BestZeroMatch:
    zero_amount:int = 0
    axis:str = "horizontal"     # "horizontal" or "vertical"
    coordinate:int = 0

def matrix_determinant(matrix:List[List[int]], dim:int) -> int:
    """Calculates matrix determinant

    Args:
        matrix (List[List[int]]): matrix
        dim (int): matrix's length

    Returns:
        int: matrix's determinant value
    """
    best_zero_match = BestZeroMatch()
    
    # TODO fine-tune this value
    min_zero_dim_search = 0
    
    # check if matrix contains zeroes
    zero_flag = False
    for row in matrix:
        if 0 in row:
            zero_flag = True
            break
    # check for least zero row or column if exists
    if zero_flag and dim > min_zero_dim_search:
        # iterate matrix horizontally
        for row_id, row in enumerate(matrix):
            if 0 in row:
                zero_count = row.count(0)
                # if any row consists of zeroes, determinator will be 0
                if zero_count == dim:
                    return 0
                if zero_count > best_zero_match.zero_amount:
                    best_zero_match.zero_amount = zero_count
                    best_zero_match.axis = "horizontal"
                    best_zero_match.coordinate = row_id
        # iterate matrix vertically
        for row_id in range(dim):
            zero_count = 0
            for column_id in range(dim):
                if matrix[column_id][row_id] == 0:
                    zero_count += 1
            # if any column consists of zeroes, determinator will be 0
            if zero_count == dim:
                return 0
            if zero_count > best_zero_match.zero_amount:
                best_zero_match.zero_amount = zero_count
                best_zero_match.axis = "vertical"
                best_zero_match.coordinate = row_id

    # calculate determinant
    determinant = 0
    for i in range(dim):
        if best_zero_match.axis == "horizontal":
            row = best_zero_match.coordinate
            id = i
        elif best_zero_match.axis == "vertical":
            row = i
            id = best_zero_match.coordinate
        modifier = -1**(row+id) * matrix[row][id]
        determinant += modifier * minor(matrix, dim, id, row)
    return determinant

def minor(matrix:List[List[int]], dim:int, x:int, y:int) -> int:
    """Calculates minor determinant

    Args:
        matrix (List[List[int]]): matrix
        dim (int): matrix's length
        x (int): x coordinate of main element
        y (int): y coordinate of main element

    Returns:
        int: minor determinant value
    """
    determinator = 0
    # iterate positively
    for i in range(dim):
        # skip if iterating on main cross-section
        if i == y or i == x:
            continue
        j = i+1
        local_determinator = 1
        for _ in range(dim):
            # id wrap
            if i == dim: i = 0
            if j == dim: j = 0
            # if item is zero, local determinator is also zero
            if matrix[i][j] == 0:
                local_determinator = 0
                break
            else:
                local_determinator *= matrix[i][j]
                i, j += 1, 1
        determinator += local_determinator
    # iterate negatively
    for i in range(dim):
        # skip if iterating on main cross-section
        if i == y or i == x:
            continue
        j = i-1
        local_determinator = 1
        for _ in range(dim):
            # id wrap
            if i == -1: i = dim-1
            if j == -1: j = dim-1
            # if item is zero, local determinator is also zero
            if matrix[i][j] == 0:
                local_determinator = 0
                break
            else:
                local_determinator *= matrix[i][j]
                i, j -= 1, 1
        determinator -= local_determinator
    return determinator

def transpose(matrix:List[List[int]], dim:int) -> List[List[int]]:
    """Transposes matrix

    Args:
        matrix (List[List[int]]): matrix
        dim (int): matrix's length

    Returns:
        List[List[int]]: transposed matrix
    """
    for i in range(dim):
        for j in  range(dim):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix