def lone_sum(a, b, c):
  count = 0
  
  if a != b and a != c:
    count += a
    
  if b != a and b != c:
    count += b

  if c != a and c != b:
    count += c
  
  return count
