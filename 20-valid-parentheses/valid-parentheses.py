class Solution(object):
    def isValid(self, s):
        
        closing_order = []

        for i in s:

            if i == ')' or i == ']' or i == '}':
                if not closing_order or i != closing_order[0]:
                    return False
                else:
                    closing_order.pop(0)
            else:
                if i == '(':
                    closing_order.insert(0,')')
            
                elif i == '{':
                    closing_order.insert(0,'}')

                else:
                    closing_order.insert(0,']')
            
        if not closing_order:
            return True
        else:
            return False