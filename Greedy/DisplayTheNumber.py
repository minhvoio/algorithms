# Link to problem: https://vjudge.net/contest/614407#problem/B

# You have a large electronic screen which can display up to 998244353
#  decimal digits. The digits are displayed in the same way as on different electronic alarm clocks: each place for a digit consists of 7
#  segments which can be turned on and off to compose different digits. The following picture describes how you can display all 10
#  decimal digits:



# As you can see, different digits may require different number of segments to be turned on. For example, if you want to display 1
# , you have to turn on 2
#  segments of the screen, and if you want to display 8
# , all 7
#  segments of some place to display a digit should be turned on.

# You want to display a really large integer on the screen. Unfortunately, the screen is bugged: no more than 𝑛
#  segments can be turned on simultaneously. So now you wonder what is the greatest integer that can be displayed by turning on no more than 𝑛
#  segments.

# Your program should be able to process 𝑡
#  different test cases.

# Input
# The first line contains one integer 𝑡
#  (1≤𝑡≤100
# ) — the number of test cases in the input.

# Then the test cases follow, each of them is represented by a separate line containing one integer 𝑛
#  (2≤𝑛≤105
# ) — the maximum number of segments that can be turned on in the corresponding testcase.

# It is guaranteed that the sum of 𝑛
#  over all test cases in the input does not exceed 105
# .

# Output
# For each test case, print the greatest integer that can be displayed by turning on no more than 𝑛
#  segments of the screen. Note that the answer may not fit in the standard 32
# -bit or 64
# -bit integral data type.

# Sample 1
# Input
# 2
# 3
# 4

# Output
# 7
# 11

# --------------------------------
# SOLUTION

test_cases = int(input())

for _ in range(test_cases):
    ans = ""
    n = int(input())

    
    numbers_of_1 = n // 2

    if n % 2 == 1:
        ans = "7"
        for i in range(1, numbers_of_1):
            ans += "1"
    
    else: 
        for i in range(numbers_of_1):
            ans += "1"

    print(ans)