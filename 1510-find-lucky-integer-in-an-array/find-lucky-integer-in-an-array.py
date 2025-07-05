class Solution(object):
    def findLucky(self, arr):
        lucky_number = -1
        
        arr_map = {}

        for int in arr:
            freq = 1
            if arr_map.get(int) != None:
                freq = freq + arr_map[int]
            arr_map.update({int:freq})

        for key, value in arr_map.items():
            if key == arr_map[key] and key > lucky_number:
                lucky_number = key

        return lucky_number
         