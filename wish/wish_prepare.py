#!/usr/bin/python
# -*- coding:utf8 -*-

# leetcode 74
# search a 2D matrix
def searchMatrix(matrix, target):
    # time: O(n*m); space: O(1)
    # edge case - matrix is empty / smaller than smallest / larger than largest
    if not matrix or not matrix[0]:
        return False
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False
    # main function
    # we can expand the whole matrix into an array and do binary search
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m*n-1
    while left <= right:
        mid = (left+right) // 2  # -> mid int number
        i, j = mid//n, mid % n  # i -> row index; j -> col index
        if matrix[i][j] == target:
            return True
        if matrix[i][j] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False  # no target being found

# leetcode 240
# search a 2D matrix2
def searchMatrix2(matrix, target):
    # time: O(m*n); space: O(1)
    # edge case - matrix is empty / smaller than smallest / larger than largest
    if not matrix or not matrix[0]:
        return False
    if target < matrix[0][0] or target > matrix[-1][-1]:
        return False
    # main function
    # starting from the top right corner; if target > current -> move down a row; else -> move left a column
    m, n = len(matrix), len(matrix[0])
    i, j = 0, n-1  # i -> row; j -> column
    while i < m and j >= 0:
        current = matrix[i][j]
        if current == target:
            return True
        if target < current:
            j -= 1
        else:
            i += 1
    return False  # we cannot find it


"""
vo1：算法。
有n个人参加跑步比赛，求有多少种排名方式，注意可能有tie。
例如，有A, B两个人，应返回3 （排名顺序可能是(1) A第一, B第二; (2) B第一, A第二; (3) AB都是第一）。
"""
def runningGame(n):
    # time: O(N^2), space: O(N^2)
    # edge case
    # 1 people -> 1 solution
    if n <= 2:
        return n
    # main function
    # create a dp -> dp[i][j] = i people in j group
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(1, i+1):
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) * (j+1)
    return sum(dp[-1])
def runningGameSpaceOptimize(n):
    # time: O(N^2), space: O(N)
    # edge case
    # 1 people -> 1 solution
    if n <= 2:
        return n
    # main function
    # create a dp -> dp[i][j] = i people in j group
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n):
        newdp = [0 for _ in range(n)]
        newdp[0] = 1
        for j in range(1, i+1):
            newdp[j] = (dp[j-1] + dp[j]) * (j+1)
        dp = newdp
    return sum(dp)
# print(runningGameSpaceOptimize(3)) # 13

"""
vo2： 设计一个feature。用户可以给product投票，如果你投票的product排名在所有参与投票的product的前10
你可以在所有参与投票的product种选择一种，0元购买。

recaptcha / rate limiter -> prevent user from spamming clicks
vote -> has to be logged in -> can only vote once
non-logged in user -> click on vote -> force to log in

intersection table (write in if vote success)
- vote time
- user id
- product id

api POST /vote
user id; product id; vote time; 
response 
success 200
500 -> voted before; 

load balancing; 
"""

# leetcode 174
# first all >= number
def calculateMinimumHP1(matrix):
    # edge case
    if not martix or not matrix[0]:
        return 0
    # main function
    dp = []
    for n in matrix[0]:
        if not dp:
            dp.append(n)
        else:
            dp.append(dp[-1] + n)
    for i in range(1, len(matrix)):
        new_dp = []
        for j, n in enumerate(matrix[i]):
            if not new_dp:
                new_dp.append(n)
            else:
                new_dp.append(n + min(new_dp[-1], dp[j]))
        dp = new_dp
    return dp[-1] + 1
# follow up incldue negative number
def calculateMinimumHP2(matrix):
    # edge case
    if not matrix or not matrix[0]:
        return 0
    # main function
    m, n = len(matrix), len(matrix[0])
    dp = [[inf for _ in range(n)] for _ in range(m)]

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1:
                if j == n-1:
                    dp[i][j] = max(1 - matrix[i][j], 1)
                else:
                    dp[i][j] = max(dp[i][j+1] - matrix[i][j], 1)
            else:
                if j == n-1:
                    dp[i][j] = max(dp[i+1][j] - matrix[i][j], 1)
                else:
                    dp[i][j] = max(
                        min(dp[i+1][j], dp[i][j+1]) - matrix[i][j], 1)

    return dp[0][0]
