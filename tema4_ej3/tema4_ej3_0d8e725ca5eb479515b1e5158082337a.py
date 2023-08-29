def jerigonzo(a):
  trans=""
  for letra in a:
      if letra in "AEIOUaeiou":
          trans+=letra
          trans+="p"
      trans+=letra
  return trans
         