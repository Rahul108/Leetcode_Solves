class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits)-1
        number = 0
        for i in digits:
            number += i*(10**length)
            length-=1
        
        number += 1
        return list(str(number))
        