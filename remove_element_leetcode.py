
def remove_element(nums: list[int], val: int) -> int:

    nums[:] = [n for n in nums if n != val]
    
    k = 0
    for o in nums:
        if o != val:
            k+=1
    
    return k

    #print(k, nums)


remove_element([3,2,2,3], 3)
remove_element([0,1,2,2,3,0,4,2], 2)

