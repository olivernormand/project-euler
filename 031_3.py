def generate_pertubations(target, coins):
    dp = [0] * (target + 1)

    dp[0] = 1

    for coin in coins:
        print("Coin: ", coin)
        for target_value in range(coin, target + 1):
            print("Target Value: ", target_value)
            dp[target_value] += dp[target_value - coin]

    return dp

if __name__ == '__main__':
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    dp = generate_pertubations(target, coins)

    for i, value in enumerate(dp):
        print(i, value)