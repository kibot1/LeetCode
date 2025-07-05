class Solution(object):
    def findLucky(self, arr):
        lucky_number = -1
        skip = []

        for x in arr:
            if x in skip:
                continue
            temp = x
            freq = 0
            for y in arr:
                if y == temp:
                    freq += 1
            if temp == freq and temp > lucky_number:
                lucky_number = temp

            freq = 0
            skip.append(temp)

        return lucky_number
        
