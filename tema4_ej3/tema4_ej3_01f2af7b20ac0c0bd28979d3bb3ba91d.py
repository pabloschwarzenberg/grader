def jerigonzo(jg):
  separador = ""
  for letras in jg:
    if letras in "AEIOUaeiou": 
      separador += letras
      separador += "p"
    separador += letras
  return separador