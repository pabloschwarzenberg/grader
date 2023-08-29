def buscarTodas (a,b):
  indiceFuncion = "" 
  num = 0 
  for x in a: 
    numString = str(num)
    if x == b: 
      if indiceFuncion == "": 
        indiceFuncion += numString 
      else: 
        indiceFuncion += " "
        indiceFuncion += numString 
    num +=1
  return indiceFuncion