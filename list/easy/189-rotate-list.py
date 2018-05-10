# -*- coding:utf-8 -*-


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 旋转方法
        def swap(start, end):
            if start == end:
                return
            i = 0
            # 以开始和结束参数的中间点为界，两端交换值
            while i<=(end-start)/2:
                nums[start+i], nums[end-i] = nums[end-i], nums[start+i]
                i = i+1

        length = len(nums)
        # 确保k小于数组长度
        k = k%length
        # k为0时不做操作
        if k != 0:
            # 把数组分为两部分，0到length-k-1和length-k到length-1，分别旋转，最后再整体旋转
            swap(0, length-k-1)
            swap(length-k, length-1)
            swap(0, length-1)
