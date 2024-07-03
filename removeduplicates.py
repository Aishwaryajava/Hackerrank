# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
# initialize a pointer that starts at element 1 
        i = 1
# for loop to iterate over the array and compare with previous element
        for j in range (1,len(nums)):
            if nums[j] != nums[j-1]:
# comparing the pointerj with previous element, if they are not the same we place the j element value in the place of i 
                nums [i]=nums[j]
                i+=1
        return i

        
        