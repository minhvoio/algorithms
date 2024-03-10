# Link to problem: https://vjudge.net/contest/614407#problem/A
# During your journey through computer universes, you stumbled upon a very interesting world. It is a path with 𝑛
#  consecutive cells, each of which can either be empty, contain thorns, or a coin. In one move, you can move one or two cells along the path, provided that the destination cell does not contain thorns (and belongs to the path). If you move to the cell with a coin, you pick it up.

# Here, green arrows correspond to legal moves, and the red arrow corresponds to an illegal move.
# You want to collect as many coins as possible. Find the maximum number of coins you can collect in the discovered world if you start in the leftmost cell of the path.

# Input
# The first line of input contains a single integer 𝑡
#  (1≤𝑡≤1000
# ) — the number of test cases. Then the descriptions of the test cases follow.

# The first line of each test case contains a single integer 𝑛
#  (1≤𝑛≤50
# ) — the length of the path.

# The second line of each test case contains a string of 𝑛
#  characters, the description of the path. The character '.' denotes an empty cell, '@' denotes a cell with a coin, and '*' denotes a cell with thorns. It is guaranteed that the first cell is empty.

# Output
# For each test case, output a single integer, the maximum number of coins you can collect.

# Sample 1
# Input
# 3
# 10
# .@@*@.**@@
# 5
# .@@@@
# 15
# .@@..@***..@@@*

# Output  
# 3
# 4
# 3

# --------------------------------
# SOLUTION

t = int(input())

for _ in range(t):
  n = int(input())  
  cells = input()
  coins = 0
  spike = False

  for i in range(1, n):
    if cells[i] == "*":
      if spike:
        break
      spike = True
    
    else:
      if cells[i] == "@":
        coins += 1
      spike = False
  
  print(coins)