class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #零钱表
        cash = [0,0]
        for i in range(len(bills)):
            if bills[i] == 5:
                cash[0] += 1
            elif bills[i] == 10 and cash[0] > 0:
                cash[0] -= 1
                cash[1] += 1
            elif bills[i] == 20 and cash[1] > 0 and cash[0] > 0:
                cash[0] -= 1
                cash[1] -= 1
            elif bills[i] == 20 and cash[1] == 0 and cash[0] > 2:
                cash[0] -= 3
            else:
                return False
        return True