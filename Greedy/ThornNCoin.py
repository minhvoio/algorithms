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