class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_total = 0
        length = len(prices)
        if length == 0:
            return max_total
        low = prices[0]
        for i in range(1,length):
            if low > prices[i]:
                low = prices[i]
            if max_total < prices[i]-low:
                max_total = prices[i]-low
        return max_total
