def buscarTodas (A,B):
  indiFun = "" 
  num = 0 
  for x in A: 
    NString = str(num)
    if x == B: 
      if indiFun == "": 
        indiFun += NString 
      else: 
        indiFun += " "
        indiFun += NString 
    num +=1
  return indiFun