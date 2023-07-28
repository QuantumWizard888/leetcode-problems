
def reverse_int(x: int) -> int:
    
    if x == 0:
        return x

    x = str(x)

    if int(x) > 0:
        
        x = int(x[::-1])
    
    elif int(x) < 0:

        x = int('-' + x[:0:-1])

    return x if -2147483648 <= x <= 2147483647 else 0


reverse_int(123)
reverse_int(-123)
reverse_int(120)
reverse_int(-120)
reverse_int(0)