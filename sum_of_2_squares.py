
from math import sqrt

def sum_of_2_squares(c: int) -> bool:
    
    if c == 0 or c == 1:
        #print('True')
        return True
    
    for i in range(c+1):
            if i*i > c:
                 #print('False')
                 return False
            elif (sqrt(c - i*i)).is_integer():
                #print('True')
                return True

sum_of_2_squares(5)
sum_of_2_squares(3)
sum_of_2_squares(1)