class Solution(object):
    def longestCommonPrefix(self, strs):
        
        result = ""
        shortest = len(strs[0])

        for word in strs:
            shortest = min(shortest,len(word))

        index = 0

        for i in range(shortest):

            comparator = strs[0][index]

            for word in strs[1:]:
                if word[index] != comparator:
                    return result
            
            result += comparator
            index += 1


        return result
        