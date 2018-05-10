class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)
        for i in range(length-1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
            else:
                digits[i] = digits[i] + 1
                break
        return digits
