def count_hi(str):
  
  count = 0
  
  length = len(str)

  for i, letter in enumerate(str):
    if letter == "h":
      if length -1 == i:
        break
      if str[i+1] == "i":
        count += 1
        
  return count
