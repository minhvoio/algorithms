import random

def generate_random_list(n: int):
  """
  n: positive integer value
  Returns random number k and list_n of 2n unique positive integers.
  """
  list_n = []
  for _ in range(n*2):
    temp = random.getrandbits(n)

    # Perform Binary Search
    while temp in list_n:
      temp = random.getrandbits(n)
    
    list_n.append(temp)

  k = random.getrandbits(n)
  return k, list_n

def search_k(k: int, list_n: list[int]):
  """
  k: positive integer number
  list_n: list of positive integers.
  Returns (True, n_steps) if k exists, and (False, n_steps) otherwise,
  where n_steps is the number of steps needed.
  """
  list_n.sort()

  # If k is equal to the minimum or the maximum number in the list, return True, 1
  if k == list_n[0] or k == list_n[-1]:
      return True, 1
  
  # Perform Binary Search
  left = 0
  right = len(list_n) - 1
  n_steps = 0

  while left <= right:
    n_steps += 1
    mid = (left + right) // 2

    if k == list_n[mid]:
      return (True, n_steps)
    
    elif k < list_n[mid]:
      right = mid - 1
    else:
      left = mid + 1

  return (False, n_steps)

def less_than_k(k: int, list_n: list[int]):
  """
  k: positive integer number
  list_n: list of positive integers.
  Return (list_nk, n_steps), where list_nk contains all numbers in list_n that 
  are less than k (if any), n_steps is the number of steps needed.
  """
  list_n.sort()

  k_exist, n_steps = search_k(k, list_n)

  if not k_exist:    
    return [], 1

  else: 

    # If k is equal to the minimum number in the list, return
    if k == list_n[0]:
      return [list_n[0]], 1    
    
    # If k is equal or larger to the maximum number in the list, return 
    if k >= list_n[-1]:
      return list_n, 1
    
    list_nk = []

    checkIndex = 0
    while list_n[checkIndex] <= k:
      list_nk.append(list_n[checkIndex])
      n_steps += 1
      checkIndex += 1

    return (list_nk, n_steps)

# Example:
k, list_n = generate_random_list(3)
k_exist = search_k(k, list_n)
list_nk = less_than_k(k, list_n)
print(k, list_n)
print(k_exist)
print(list_nk)

# # Output
# 5, [3, 2, 5, 1, 6, 7]
# (True, 3)
# ([2, 1], 6)