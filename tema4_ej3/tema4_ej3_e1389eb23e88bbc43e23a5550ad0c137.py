def jerigonzo(string):
  jerigonzo=""
  for letra in string:
     if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
       jerigonzo=jerigonzo+letra+"p"+letra
     else:
       jerigonzo=jerigonzo+letra
  return jerigonzo
  
if __name__ == "__main__":
   string=input("Inserte texto a traducir:")
   print(jerigonzo(string))
   
   
         