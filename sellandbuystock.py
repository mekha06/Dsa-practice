#Best Time to Buy and Sell Stock
price = list(map(int, input("enter the array elements : ").split()))
min_price = price[0]
max_profit = 0
buy_price = price[0]
sell_price = price[0]
for i in range(1, len(price)):
    if price[i] < min_price:
        min_price = price[i]
    profit = price[i] - min_price
    if profit > max_profit:
        max_profit = profit
        buy_price = min_price
        sell_price = price[i]
print(f"maximum profit is {max_profit}")
print(f"buy at {buy_price} and sell at {sell_price}")

"""
---------------------------------------------Output---------------------------------------------
enter the array elements : 7 1 5 3 6 4
maximum profit is 5
buy at 1 and sell at 6

TC=O(n)
You are given stock prices for different days [7 1 5 3 6 4]
You can:buy only once,sell only once and buying must happen before selling
Goal:Find the maximum possible profit.

Optimal Solution Idea:Traverse the array once while
-tracking the minimum price seen so far
-calculating profit if sold today
-updating maximum profit

At every day: profit = current price - minimum buying price so far
If this profit is larger,update maximum profit

"""