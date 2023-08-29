def rot13(palabra):
  P_Rot13 = ""
  for L in P_Rot13:
    if L >= "a" and L <= "z":
      Num_Letra = ord(L)
      Rotacion = Num_Letra+13
      if Rotacion <=112:
        P_Rot13 = P_Rot13 + chr(Rotacion)
      else:
        Rotacion = 97 + (Rotacion-123)
        P_Rot13 = 97 + (Rotacion-123)
    else:
      P_Rot13 = P_Rot13 + 1
  return P_Rot13    
