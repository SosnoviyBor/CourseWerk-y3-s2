class Matrix:
    def __init__(self, mat):
        self.mat = mat

    # handy method to print the matrix to the console
    def print(self):
        for i in self.mat:
            for j in i:
                print(j, end=" ")
            print('')

    # add the identity matrix to the original matrix from the right
    def add_identity_matrix(self):
        n = len(self.mat)
        for i in range(n):
            for j in range(n):
                if i == j:
                    self.mat[i].append(1)
                else:
                    self.mat[i].append(0)
        return self.mat

    # remove the identity matrix - after inverting - from the left
    def remove_identity_matrix(self):
        n = len(self.mat)
        new_mat = []
        for i in range(n):
            new_mat.append(self.mat[i][n:])
        self.mat = new_mat

    # invert the matrix
    def inverse(self):
        n = len(self.mat)

        # Handling the 2x2 matrix inverse
        if n == 2:
            det = self.mat[0][0]*self.mat[1][1] - self.mat[0][1]*self.mat[1][0]
            new_mat = [
                [self.mat[1][1], -self.mat[0][1]],
                [-self.mat[1][0], self.mat[0][0]]
            ]
            for i in range(n):
                for j in range(n):
                    new_mat[i][j] /= det
            self.mat = new_mat
            return

        aug_mat = self.add_identity_matrix()
        aug_n = n*2

        for i in range(n):
            # main diagonal element on row i
            pivot = aug_mat[i][i]

            # divide whole row of augmented matrix by diagonal element
            for a in range(aug_n):
                aug_mat[i][a] = aug_mat[i][a] / pivot

            # for each row except row i
            for j in range(n):
                if j != i:
                    target = aug_mat[j][i]
                    ratio = -target / pivot
                    # for each element in column k
                    for k in range(aug_n):
                        aug_mat[j][k] += ratio * aug_mat[i][k]
        self.remove_identity_matrix()