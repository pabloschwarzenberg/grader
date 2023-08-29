def jerigonzo(string):
  vocales = ['a','e','i','o','u']
  j_string = list(string)
  j = 0
  palabra_jerigoncio = []
  while j < len(string):
    if bool(j_string[j] in vocales) == False:
      palabra_jerigoncio.insert(j,j_string[j])
    elif bool(j_string[j] in vocales) == True:
      palabra_jerigoncio.append("{}{}{}".format(j_string[j],'p',j_string[j]))
    j = j + 1
    
  st = ''.join(palabra_jerigoncio)
  return st

         