R = 3
C = 3

def min_cost(cost, m, n):
    # Initialize a DP table with zeros
    dp = [[0 for _ in range(C)] for _ in range(R)]

    # Base case: starting cell
    dp[0][0] = cost[0][0]

    # Fill first column (only one way to reach these cells)
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] + cost[i][0]

    # Fill first row (only one way to reach these cells)
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] + cost[0][j]

    # Fill the rest of the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + cost[i][j]

    return dp[m][n]
