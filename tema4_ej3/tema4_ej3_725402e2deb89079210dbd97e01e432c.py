def jerigonzo(string):
  translado=""
  for letra in string:
      if letra in "AEIOUaeiou":
          translado+=letra
          translado+="p"
      translado+=letra
  return translado