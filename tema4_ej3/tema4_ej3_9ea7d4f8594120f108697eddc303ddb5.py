def jerigonzo(string):
  vocales = ['a','e','i','o','u']
  traduccion = ''
  last= 0
  for i in range(len(string)):
    if string[i] in vocales:
      traduccion = traduccion + string[last:i+1] + 'p' + string[i]
      last = i+1
  string = traduccion
  return string