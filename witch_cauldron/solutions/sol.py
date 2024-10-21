def witch_cauldron_combination_lock(ingredients, target_weight):
    dp = [-1] * (target_weight + 1)
    dp[0] = 0

    # Loop through each ingredient
    for weight, value in ingredients:
        # Traverse the dp array from back to front to ensure we don't reuse the same item more than once.
        for w in range(target_weight, weight - 1, -1):
            if dp[w - weight] != -1:
                dp[w] = max(dp[w], dp[w - weight] + value)

    # The answer is the maximum value achievable at exactly `target_weight`.
    return dp[target_weight] if dp[target_weight] != -1 else -1


def main():
    n, weight = map(int, input().split())
    ingredients = []
    for _ in range(n):
        ingredients.append(tuple(map(int, input().split())))
    print(witch_cauldron_combination_lock(ingredients, weight))


if __name__ == "__main__":
    main()
