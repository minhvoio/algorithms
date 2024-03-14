# Link to problem: https://vjudge.net/contest/614407#problem/#
# In a movie festival, 
# n movies will be shown. Syrjälä's movie club consists of 
# k members, who will be all attending the festival.

# You know the starting and ending time of each movie. What is the maximum total number of movies the club members can watch entirely if they act optimally?

# Input
# The first input line has two integers 
# n and 
# k: the number of movies and club members.

# After this, there are 
# n lines that describe the movies. Each line has two integers 
# a and 
# b: the starting and ending time of a movie.

# Output
# Print one integer: the maximum total number of movies.

# Constraints
# 1≤k≤n≤2*10^5
# 1≤a<b≤10^9
 
# Example
# Input
# 5 2
# 1 5
# 8 10
# 3 6
# 2 5
# 6 9

# Output
# 4

# --------------------------------
# SOLUTION
# O(k*n)

n, k = map(int, input().split())

movies = []

for i in range(n):
  start, end = map(int, input().split())
  movies.append((start, end))

movies.sort(key = lambda x: x[1])

watched_movies = []

for _ in range(k):
  prev_end = 0
  
  for start, end in movies:
    if watched_movies.count((start, end)) == 0 and start >= prev_end:
      watched_movies.append((start, end))      
      prev_end = end  

print(len(watched_movies))