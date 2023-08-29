def jerigonzo(string):
  palabra =""
  vocal = ["a", "e", "i", "o", "u"]
  for p in string: 
    if p in vocal: 
      palabra += p
      palabra += "p"
      palabra += p
    else: 
      palabra += p
  return palabra

