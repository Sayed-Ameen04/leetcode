class Solution(object):
    def stoneGameIX(self, stones):
        r0 = r1 = r2 = 0
        for val in stones:
            if val % 3 == 0:
                r0 += 1
            elif val % 3 == 1:
                r1 += 1
            else:
                r2 += 1

        if r0 % 2 == 0:
            return r1 > 0 and r2 > 0

        return abs(r1 - r2) > 2
        