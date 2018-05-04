# -*- coding:utf-8 -*-


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        # 判断数组长度为0的情况
        if length == 0:
            return -1
        # 指针在索引0的情况下计算数组左右的值
        left = 0
        right = sum(nums)-nums[0]
        for i in range(length):
            # 如果当前的索引左边的值等于右边的值,返回索引
            if left == right:
                return i
            else:
                # 如果指针已经移动到了最右边的索引仍不能相等,返回-1
                if i == length-1:
                    return -1
                # 不等的情况下，重新计算下一个索引的左右两边的值
                left = left+nums[i]
                right = right-nums[i+1]
