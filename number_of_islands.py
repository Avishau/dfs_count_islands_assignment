import copy
"""
Assignment Title: Counting the Number of Islands

Background:
In computer science, the "Number of Islands" problem is a classic graph traversal problem 
that involves identifying distinct clusters in a grid. The task simulates real-world applications 
like image processing, social network analysis, and geographic mapping.

Problem Statement:
You are given a 2D grid of '1's (land) and '0's (water). An island is surrounded by water and is formed 
by connecting adjacent lands horizontally or vertically. You need to determine the number of islands 
in the given grid.

Task:
Write a Python function `count_islands(grid: List[List[str]]) -> int` that takes a 2D grid as input 
and returns the total number of distinct islands.

Input:
- A 2D grid represented as a list of lists of strings, where:
  - '1' represents land.
  - '0' represents water.
- The grid dimensions are at most 300 x 300.

Output:
- An integer representing the number of islands.

Example:

Input:
grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"]
]

Output:
3

Explanation:
- Island 1: Formed by the top-left cluster of '1's.
- Island 2: Formed by the middle '1'.
- Island 3: Formed by the bottom-right cluster of '1's.

Constraints:
1. The grid can contain only the characters '1' and '0'.
2. You may assume all four edges of the grid are surrounded by water.
3. The grid may contain no land ('1'), in which case the output should be 0.

Guidelines:
1. Implement the solution using either Depth-First Search (DFS).
2. Avoid visiting the same cell more than once. Use a mechanism (e.g., marking visited cells) 
   to keep track of visited land cells.
3. Test your solution with edge cases, such as an empty grid, a grid with no islands, or a grid with a single island.

Bonus Challenges:
1. Optimize the solution for memory usage in large grids.
2. Modify the function to allow diagonal connections (i.e., islands connected diagonally are considered part of the same island).
3. Visualize the grid and the islands using a plotting library like Matplotlib.

Submission:
- Save your solution in a Python file named `number_of_islands.py`.
- Include comments explaining your approach and any assumptions.
- Test your code with at least five unique test cases and include them in a separate file named `test_number_of_islands.py`.
"""

from typing import List
def dfs_count_islands(grid, visited_grid, x, y, bound_x, bound_y):

    visited_grid[y][x] = True
    #recuresive calls to neighbors:
    #UP (Check boundary and if destination is not visited):
    if y - 1 >= 0 and grid[y-1][x] == '1' and visited_grid[y-1][x] == False:
        dfs_count_islands(grid, visited_grid, x, y-1, bound_x, bound_y)

    #DOWN(Check boundary):
    if y + 1 < bound_y and grid[y+1][x] == '1' and visited_grid[y+1][x] == False:
        dfs_count_islands(grid, visited_grid, x, y+1, bound_x, bound_y)

    #LEFT(Check boundary):
    if x - 1 >= 0 and grid[y][x-1] == '1' and visited_grid[y][x-1] == False:
        dfs_count_islands(grid, visited_grid, x-1, y, bound_x, bound_y)

    #RIGHT(Check boundary):
    if x + 1 < bound_x and grid[y][x+1] == '1' and visited_grid[y][x+1] == False:
        dfs_count_islands(grid, visited_grid, x+1, y, bound_x, bound_y)






def count_islands(grid: List[List[str]]) -> int:
   # number of cols
   i = len(grid[0])
   #number of rows
   j = len(grid)
   counter = 0
   #init the visited to False
   visited_grid = [[False for _ in range(i)] for _ in range(j)]

   for y in range(j):
        for x in range(i):
            if grid[y][x] == '1' and visited_grid[y][x] == False:
                dfs_count_islands(grid, visited_grid, x, y, i, j)
                counter += 1
   return counter

# grid = [
#   ["1", "1", "0", "0", "0"],
#   ["1", "1", "0", "0", "0"],
#   ["0", "0", "1", "0", "0"],
#   ["0", "0", "0", "1", "1"]
# ]
grid = [
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0"],
  ["0", "0", "0", "0", "0"]
]
print(count_islands(grid))
   # """
   #  Counts the number of distinct islands in the given 2D grid.
   #
   #  Args:
   #      grid (List[List[str]]): A 2D grid of '1's (land) and '0's (water).
   #
   #  Returns:
   #      int: The total number of islands.
   #  """

