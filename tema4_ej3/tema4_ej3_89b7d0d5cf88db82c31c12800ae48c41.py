def jerigonzo(string):


  l = ""

  vocal= ["A","a","E","e", "I", "i", "O", "o", "U", "u"]

  for x in string:

    if x in vocal:

      l += x

      l += "p"

    l += x

  return l
