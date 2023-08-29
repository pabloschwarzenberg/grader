def jerigonzo(string):
  i=''
  for letter in string:
    if letter in 'AEIOUaeiouáéíóú':
      i+=letter
      i+='p'
    i+=letter
    return string

       