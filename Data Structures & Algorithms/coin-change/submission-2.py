class Solution:
    """
    Understand:
    Input: a list of ints
    Output: amount in int
    Edge cases: if target is zero return 0

    Plan:
    create an array of size t
    loop through the amount
        loop through the coins
            if c <= x
                update current best using min (best[x], 1 + best[x - c])
    return
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("inf")] * amount

        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    dp[x] = min(dp[x], dp[x - c] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1