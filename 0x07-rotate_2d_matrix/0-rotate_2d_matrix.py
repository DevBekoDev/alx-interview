#!/usr/bin/python3
"""script tp rotate a 2D Matrix
"""

def rotate_2d_matrix(matrix):
    """taking n x n 2D matrix,rotate the matric 90 degrees clockwise."""

    rotated = [list(row) for row in zip(*reversed(matrix))]
    
    for i in range(len(matrix)):
        matrix[i] = rotated[i]

if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
