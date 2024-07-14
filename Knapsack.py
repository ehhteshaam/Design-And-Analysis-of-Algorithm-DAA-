def maximum_value(tc, test_cases):
    results = []
    for i in range(tc):
        a, b, coins = test_cases[i]
        dp = [0] * (b + 1)
        
        for coin in sorted(coins):
            for g in range(coin, b + 1):
                dp[g] = max(dp[g], coin + dp[g - coin])
        
        results.append(dp[b])
    return results

# Example usage
if __name__ == "__main__":
    tc = int(input())
    test_cases = []
    for _ in range(tc):
        a, b = map(int, input().split())
        coins = list(map(int, input().split()))
        test_cases.append((a, b, coins))
    
    results = maximum_value(tc, test_cases)
    for result in results:
        print(result)
