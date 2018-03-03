"""
    Problem:
        Given two lists A and B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
        We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
        These lists A and B may contain duplicates. If there are multiple answers, output any of them.

        P.S: Problem description copied from: https://leetcode.com/problems/find-anagram-mappings/description/
"""
class Solution:
    def anagramMappings(self, A, B):
        return list(map(lambda x: B.index(x), A))
