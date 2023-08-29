def jerigonzo(a):
    b="aeiou"
    t=""
    for letra in a:
      if letra in b:
        t=t+letra+"p"+letra
      else: 
        t=t+letra
    return t
        

if __name__ == "__main__":
  a=input()
  print(jerigonzo(a))