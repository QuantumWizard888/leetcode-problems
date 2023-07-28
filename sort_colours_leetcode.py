
def sort_colours(nums: list[int]) -> None:

   print('Input: ', nums)

   arr_0 = [0] * nums.count(0)
   arr_1 = [1] * nums.count(1)
   arr_2 = [2] * nums.count(2)

   nums[:] = arr_0 + arr_1 + arr_2
   
   print('Output: ', nums)



print(sort_colours([2,0,2,1,1,0]))
print(sort_colours([2,0,1]))