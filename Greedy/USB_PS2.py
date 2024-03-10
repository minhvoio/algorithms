# Link to problem: https://vjudge.net/contest/614407#problem/C
# Due to the increase in the number of students of Berland State University it was decided to equip a new computer room. You were given the task of buying mouses, and you have to spend as little as possible. After all, the country is in crisis!

# The computers bought for the room were different. Some of them had only USB ports, some — only PS/2 ports, and some had both options.

# You have found a price list of a certain computer shop. In it, for m mouses it is specified the cost and the type of the port that is required to plug the mouse in (USB or PS/2). Each mouse from the list can be bought at most once.

# You want to buy some set of mouses from the given price list in such a way so that you maximize the number of computers equipped with mouses (it is not guaranteed that you will be able to equip all of the computers), and in case of equality of this value you want to minimize the total cost of mouses you will buy.

# Input
# The first line contains three integers a, b and c (0 ≤ a, b, c ≤ 105)  — the number of computers that only have USB ports, the number of computers, that only have PS/2 ports, and the number of computers, that have both options, respectively.

# The next line contains one integer m (0 ≤ m ≤ 3·105)  — the number of mouses in the price list.

# The next m lines each describe another mouse. The i-th line contains first integer vali (1 ≤ vali ≤ 109)  — the cost of the i-th mouse, then the type of port (USB or PS/2) that is required to plug the mouse in.

# Output
# Output two integers separated by space — the number of equipped computers and the total cost of the mouses you will buy.

# Sample 1
# Input
# 2 1 1
# 4
# 5 USB
# 6 PS/2
# 3 PS/2
# 7 PS/2

# Output
# 3 14
# Note
# In the first example you can buy the first three mouses. This way you will equip one of the computers that has only a USB port with a USB mouse, and the two PS/2 mouses you will plug into the computer with PS/2 port and the computer with both ports.

# --------------------------------
# SOLUTION

a, b, c = map(int, input().split())
m = int(input())  

usb_cost = []
ps2_cost = []

for _ in range(m):
    val, typ = input().split()
    val = int(val)

    if typ == 'USB':
        usb_cost.append(val)

    if typ == 'PS/2':
        ps2_cost.append(val)

usb_cost.sort(reverse = True)
ps2_cost.sort(reverse = True)

equipped = 0
cost = 0

for i in range(min(a, len(usb_cost))):
    equipped += 1
    cost += usb_cost.pop()
    

for i in range(min(b, len(ps2_cost))):
    equipped += 1
    cost += ps2_cost.pop()
    

remaining_mice = usb_cost + ps2_cost
remaining_mice.sort()

for i in range(min(c, len(remaining_mice))):
    equipped += 1
    cost += remaining_mice[i]

print(equipped, cost)