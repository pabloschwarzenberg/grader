def jerigonzo(palab):
  conta = ""
  for let in palab:
    if let in "AEIOUaeiou": 
      conta += let
      conta += "p"
    conta += let
  return conta