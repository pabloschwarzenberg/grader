def rot13(palabra):
  alfabeto= "abcdefghijklmnopqrstuvwxyz"
  string = ""
  for i in palabra:
    if i in alfabeto:
      if alfabeto.index(i) <13:
        string += alfabeto [alfabeto.index(i) + 13]
      else: string+= alfabeto[alfabeto.index(i) -13]
    elif i in alfabeto.upper():
      if alfabeto.upper().index(i) <13:
            string += alfabeto.upper()[alfabeto.upper().index(i) + 13]
      else: string+= alfabeto.upper()[alfabeto.upper().index(i) - 13]
      
    else: string += i
  return string
           