def jerigonzo(b):
  translado=""
  for letra in b:
      if letra in "AEIOUaeiou":
          translado+=letra
          translado+="p"
      translado+=letra
  return translado