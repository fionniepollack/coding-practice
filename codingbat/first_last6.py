def first_last6(nums):

  for num in nums:
    if nums[0] == 6 or nums[-1] == 6:
      return True
  
  return False
