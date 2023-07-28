
def add_numbers(num1: list, num2: list) -> list:
    
    num1 = int(''.join([str(n) for n in num1[::-1]]))
    num2 = int(''.join([str(n) for n in num2[::-1]]))
    result = [int(n) for n in list(str(num1 + num2))[::-1]]

    return result
    #print(num1, num2)
    #print(result)

add_numbers([2,4,3], [5,6,4])
add_numbers([0], [0])
add_numbers([9,9,9,9,9,9,9], [9,9,9,9])