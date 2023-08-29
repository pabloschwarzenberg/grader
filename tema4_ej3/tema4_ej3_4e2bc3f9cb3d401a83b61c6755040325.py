def jerigonzo(Palabras_Texto):
    Condicion =""
    for Letras in Palabras_Texto:
        if Letras == 'a' or Letras == 'e' or Letras == 'i' or Letras == 'o' or Letras == 'u':
            Condicion = Condicion + Letras + "p" + Letras
        else:
            Condicion = Condicion + Letras        
    return Condicion
         