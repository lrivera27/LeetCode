"""
    Problem:
        The Hamming distance between two integers is the number of positions at
        which the corresponding bits are different.
        Given two integers x and y, calculate the Hamming distance.

        P.S: Problem description copied from: https://leetcode.com/problems/hamming-distance/description/
"""

class Solution:
    def hammingDistance(self, x, y):
        x = list("{0:b}".format(x))
        y = list("{0:b}".format(y))
        if len(x) > len(y):
            y = ['0' for i in range(len(x) - len(y))] + y
        elif len(y) > len(x):
            x = ['0' for i in range(len(y) - len(x))] + x
        counter = 0
        for first, second in zip(x, y):
            if(first != second):
                counter += 1
        return counter


test = Solution()
print(test.hammingDistance(6, 11))



#   list x => 0 1 1 0
#   list y => 1 0 1 1
#   x - y = 3 =? 3 zeroes need to be added
