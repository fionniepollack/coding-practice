def centered_average(nums):

  max_num = max(nums)
  min_num = min(nums)

  for i, num in enumerate(nums):
    if num == max_num:
      nums.pop(i)
      for i, num in enumerate(nums):
        if num == min_num:
          nums.pop(i)

  return sum(nums)/len(nums)
