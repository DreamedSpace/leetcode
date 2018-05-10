class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        total = []
        # 用total保存位置为i时的最大值
        total.append(nums[0])
        # 初始化数组长度为1时的最大值值
        max_total = total[0]
        for i in range(1, length):
            # 如果在i-1位置得到的值小于0,说明后面的值再加它已经没有必要了，就从新的值nums[i]作为i位置的最大值
            if total[i-1] <= 0:
                total.append(nums[i])
            else:
                # 如果i-1位置得到的值大于0,则后面的值还需要加上它
                total.append(nums[i] + total[i-1])
            # 随时更新最大值
            if total[i] > max_total:
                max_total = total[i]
        return max_total
