import numpy as np


def snake(m, n):
    matrix = np.zeros((m, n), dtype=int)

    for i in range(m):
        array = np.arange(1, m * n + 1)
        
        matrix = array.reshape(m, n)

        for i in range(1, m, 2):
            matrix[i] = matrix[i][::-1]

        return matrix