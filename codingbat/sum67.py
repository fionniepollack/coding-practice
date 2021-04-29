def sum67(nums):

  total = 0
  skip_num = False

  for num in nums:

    if num == 6:
      skip_num = True
      continue

    if num == 7 and skip_num is True:
      skip_num = False
      continue

    if skip_num is False:
      total += num

  return total
