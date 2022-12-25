def Goodpairs(nums):
    counter = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i < j and nums[i] == nums[j]:
                counter = counter + 1
    return counter
print(Goodpairs([1,2,3,1,1,3]))
print(Goodpairs([1,2,3]))
