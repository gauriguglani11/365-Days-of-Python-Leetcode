#Logic
#1. Sort the Cost array so that we can buy maximum low cost Ice Cream Bars
#2. Buy the low cost Ice Cream Bars and reduce the coins as you buy
#This function takes in two arguments:

coins: the number of coins the boy has
costs: a list of integers representing the price of each ice cream bar in coins
It returns the maximum number of ice cream bars that the boy can buy with the given number of coins.

The function first sorts the list of costs in ascending order. Then, it uses a loop to iterate through the list of costs and checks if the boy has enough coins to buy the current ice cream bar. 
If he does, the max_icecreams variable is incremented by 1 and the number of coins is decremented by the cost of the ice cream bar. If the boy does not have enough coins, the loop is broken and the 
function returns the current value of max_icecreams.

code:
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        result=0
        costs.sort()
        for x,y in enumerate(costs):
            if coins<y:
                break
            result = result + 1
            coins = coins - y
        return result