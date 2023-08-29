def jerigonzo(palabruh):
  contd = ""
  for letra in palabruh:
    if letra in "AEIOUaeiou": 
      contd += letra
      contd += "p"
    contd += letra
  return contd