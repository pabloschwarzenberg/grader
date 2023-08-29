def jerigonzo(a):
  translado=""
  for letra in a:
      if letra in "AEIOUaeiou":
          translado+=letra
          translado+="p"
      translado+=letra
  return translado