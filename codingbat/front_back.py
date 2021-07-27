def front_back(str):
  
  if len(str) <= 1:
    return str
    
  first_char = str[0]
  middle_chars = str[1:len(str)-1]
  last_char = str[-1]

  new_string = last_char + middle_chars + first_char
  
  return new_string
