
def remove_duplicates(nums: list) -> int:

    nums[:] = list(set(nums))
    nums.sort()
    #print(nums)
    #print(len(nums), nums)

    return len(nums)


remove_duplicates([1,1,2])
remove_duplicates([0,0,1,1,1,2,2,3,3,4])
remove_duplicates([-1,0,0,0,0,3,3])
