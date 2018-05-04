# -*- coding:utf-8 -*-


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        # 动态规划相关
        length = len(cost)
        # 长度为2时的判断
        if length == 2:
            return cost[0] if cost[0]<cost[1] else cost[1]
        # 声明记录花费的数组c,并依次添加c[0]和c[1]均为0
        c = []
        c.append(0)
        c.append(0)
        i = 2
        # 数组长度大于2时的处理,比较(当前位置前一位的花费+到前一位的花费)和(当前位置前两位+到前两位的花费),哪个小就作为到当前位置的花费
        while i <= length:
            if c[i-1]+cost[i-1] > c[i-2]+cost[i-2]:
                c.append(c[i-2]+cost[i-2])
            else:
                c.append(c[i-1]+cost[i-1])
            i = i+1
        # 返回最终的花费,由于走完楼梯是要超出楼梯这个数组的,所以花费数组比楼梯数组长一位
        return c[length]
