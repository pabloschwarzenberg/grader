#Ordenar tres números
a = int(input("ingrese su primer numero"))      
b = int(input("ingrese su segundo numero"))
c = int(input("ingrese su tercer numero"))

if c <= b and b <= a :
   print("%d ,%d ,%d" %(c,b,a))
else:
     if b < c and c < a:
        print("%d ,%d ,%d" %(b , c , a))
     else:
          if a <= c and c <= b:
              print("%d ,%d ,%d" %(a , c , b))
          else:
               if c <= a and a <= b:
                   print("%d ,%d ,%d" %(c , a , b))
               else:
                    if b <= a and a <= c:
                        print("%d ,%d ,%d" %(b , a , c))
                    else:
                         if a <= b and b <= c:
                             print("%d ,%d ,%d" %(a , b , c))
                 
            