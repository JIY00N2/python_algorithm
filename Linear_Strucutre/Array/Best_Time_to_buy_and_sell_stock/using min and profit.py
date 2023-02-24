from typing import List
import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 최댓값에는 가장 낮은 값을 초깃값으로 해야 어떤 값이든 최댓값이 교체 될 수 있고
        # 반대로 최솟값에는 가장 높은 값을 초깃값으로 해야 어떤 값이든 최솟값이 바로 교체될 수 있다.
        profit = 0
        min_price = sys.maxsize
        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)

        return profit


solution = Solution()
prices:  list = [7,1,5,3,6,4]
result: int = solution.maxProfit(prices)
print(result)