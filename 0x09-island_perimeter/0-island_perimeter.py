#!/usr/bin/python3
"""
island parameter
"""


def island_perimeter(grid):
    R, C = len(grid), len(grid[0])
    perimeter = 0
    # Traverse the grid
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                perimeter += 4
                # Check whether top neighbour is a land and decrement it by 2
                # as it intersects
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2
                # Check left neighbour is a land and decrement it by 2
                # as it intersects
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2
    return perimeter
