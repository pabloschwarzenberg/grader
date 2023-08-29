def jerigonzo(string):
  string_j=""
  for letra in string:
    if letra == "a" or letra =="e" or letra =="i" or letra =="o" or letra =="u" :
      string_j = string_j + letra +"p" + letra
    else:
      string_j = string_j + letra
    
  return string_j

if __name__ == "__main__":
    pass
         