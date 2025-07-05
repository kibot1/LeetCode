class Solution(object):
    def findLucky(self, arr):
        lucky_number = -1

        for x in arr:
            temp = x
            freq = 0
            index = 0
            for y in arr:
                if y == temp:
                    freq += 1
            if temp == freq and temp > lucky_number:
                lucky_number = temp

            freq = 0

        return lucky_number
        