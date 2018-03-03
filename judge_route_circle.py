"""
    Problem:
        Initially, there is a Robot at position (0, 0). Given a sequence of its moves,
        judge if this robot makes a circle, which means it moves back to the original place.
        The move sequence is represented by a string. And each move is represent by a character.
        The valid robot moves are R (Right), L (Left), U (Up) and D (down).
        The output should be true or false representing whether the robot makes a circle.

        P.S: Problem description copied from: https://leetcode.com/problems/judge-route-circle/description/
"""
class Solution:
    def judgeCircle(self, moves):
        position = 0
        for move in list(moves):
            if move == "U":
                position += 1
            elif move == "D":
                position -= 1
            elif move == "L":
                position += 2
            elif move == "R":
                position -= 2
        if position == 0: return True
        else: return False
