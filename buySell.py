#! /usr/bin/env python3

'''
You are given an array prices where prices[i] is the price 
of a given stock on the ith day.

You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future 
to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

'''

def buySell(prices : list):
    
    buy, sell = 0,1
    maxSell = 0
    
    while sell < len(prices):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            maxSell = max(maxSell, profit)
        else:
            buy = sell
        sell += 1
    
    return maxSell


if __name__ == '__main__':
    
    print(buySell([7,1,5,3,6,4]))
    # 5
    print(buySell([7,6,4,3,1]))
    # 0
    print(buySell([2,4,1]))
    # 2

    
