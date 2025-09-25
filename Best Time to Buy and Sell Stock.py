def maxProfit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            current_profit = prices[i] - min_price
            if current_profit > max_profit:
                max_profit = current_profit

    return max_profit
