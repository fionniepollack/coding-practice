def cigar_party(cigars, is_weekend):
  
  if not is_weekend:
    if cigars in range(40,61):
      return True
    
  else:
    if cigars >= 40:
      return True
  
  return False
