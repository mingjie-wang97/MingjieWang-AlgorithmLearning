def vo1(n):
	dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
	for i in range(1, n+1): # i people
		for j in range(1, i+1): # j group
			if i == j and i == 1:
				dp[i][j] = 1
			else:
				dp[i][j] = j * dp[i-1][j-1] + j * dp[i-1][j]
	print(dp)
	return sum(dp[-1])

print(vo1(3))

def PeopleRanking(n):
    def fac(n):
        output = []
        for i in range (1, n+1):
            if i == 1:
                output.append(1)
            else:
                output.append(i*output[-1])
        return output
    f = fac(n)
    print(f)
    dp = [[0 for i in range (n)] for i in range (n)]
    for place in range (n):
        for people in range (place, n):
            if place == 0: dp[place][people] = 1
            elif people == place: dp[place][people] = f[place]
            elif people > place and place >= 0:
                dp[place][people] = (place+1)*dp[place][people-1] + (place+1)*dp[place-1][people-1]
    print(dp)
    output = sum([x[-1] for x in dp])
    return output
print (PeopleRanking(3))
