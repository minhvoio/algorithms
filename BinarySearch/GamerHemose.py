# Link to problem: https://vjudge.net/contest/614182#problem/A

t = int(input())

def minimum_times_use_weapon():
  n, H = map(int, input().split())

  damages = []
  damages.extend(map(int, input().split()[:n]))
  damages.sort()

  ans = 0
  use_strongest_weapon = True
  while H > 0:
    ans += 1
    if use_strongest_weapon:
      H -= damages[n-1]    
      use_strongest_weapon = False
    else:
      H -= damages[n-2]
      use_strongest_weapon = True
  
  print(ans)

for _ in range(t):
  minimum_times_use_weapon()