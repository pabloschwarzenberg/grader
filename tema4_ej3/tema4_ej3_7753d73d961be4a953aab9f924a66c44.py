def jerigonzo(string):
  vocales = ['a', 'e', 'i', 'o', 'u']
  t = ""
  for i in range(len(string)):
    if string[i] in vocales:
      t += string[i] + "p" + string[i]
    else:
      t += string[i]
  return t
