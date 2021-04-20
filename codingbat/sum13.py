# Solution 1

def sum13(nums):

  total = 0
  skip_num = False

  for num in nums:

    if num == 13:
      skip_num = True
      continue
    if skip_num:
      skip_num = False
      continue
  

    else:
      total += num

  return total



# Solution 2

def sum13(nums):
  
  total = 0
  
  i = 0

  while i < len(nums):
    if nums[i] == 13:
      i += 2
      continue

    total += nums[i]
    i += 1

  return total
