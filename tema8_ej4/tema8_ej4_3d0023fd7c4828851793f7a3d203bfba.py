def rot13(palabra):
  alfa_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  alfa_min = "abcdefghijklmnopqrstuvwxyz"
  aux = ""
  
  for i in palabra:
    if i in alfa_may:    
      if alfa_may.index(i) >= 13:
        B = alfa_may.index(i) - 13
        aux = aux + alfa_may[B]     
      else:
        A = alfa_may.index(i) + 13  
        aux = aux + alfa_may[A]
    if i in alfa_min: 
      if alfa_min.index(i) >= 13:
          b = alfa_min.index(i) - 13
          aux = aux + alfa_min[b]
      else:
        a = alfa_min.index(i) + 13  
        aux = aux + alfa_min[a]
  return aux 