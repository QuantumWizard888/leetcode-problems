
arr1 = [0,1,0,2,1,0,1,3,2,1,2,1]
arr2 = [4,2,0,3,2,5]


def rain(height:list):
    max_left = 0
    max_right = 0
    maxleft_lst = []
    maxright_lst = []
    rain = 0
    
    for n in height:
        if n > max_left:
            max_left = n
            maxleft_lst.append(max_left)
        
        elif n <= max_left:
            maxleft_lst.append(max_left)


    for m in height[::-1]:
        if m > max_right:
            max_right = m
            maxright_lst.append(max_right)
        
        elif m <= max_right:
            maxright_lst.append(max_right)

    maxright_lst = maxright_lst[::-1]

    for i in range(len(height)):
        rain += min(maxleft_lst[i], maxright_lst[i]) - height[i]

    
    print(rain)


rain(arr1)
rain(arr2)