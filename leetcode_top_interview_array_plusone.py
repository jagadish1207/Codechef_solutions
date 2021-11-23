# [1,2,2,1,4,6,6]
# 9999
# 8999
# 219
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    step = 0
    for i in range(len(digits)-1,-1,-1):
        if (digits[i]==9):
            step = step+1
            digits[i] = 0
        else:
            if (step > 0):
                digits[i] = digits[i]+1
                return digits
            else:
                digits[i] = digits[i]+1
                return digits
    for i in range(0,step):
        if (i == 0):
            digits.remove(digits[0])
            digits.insert(0,1)
            digits.insert(1,0)
        else:
            digits[i] = 0
    return digits


l1 = [8,9,9]
print(plusOne(l1))