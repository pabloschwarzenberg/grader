#Juego adivina mi número
x=randint(1,20)
print("Bienvenido al juego")
a=int(input("Ingresa un número: "))
if a==x:
  print("Adivinaste, mi número era", a)
elif a!=x:
   b=int(input("Inténtalo de nuevo, ingresa otro número: ")
   if b == x :
    print("Adivinaste, mi número era", b)
   elif b!=x:
     c=int(input("Inténtalo de nuevo, ingresa otro número: ")
     if c==x:
       print("Adivinaste, mi número era", c)
     elif c!=x:
       d=int(input("Inténtalo de nuevo, ingresa otro número: ")
       if d==x:
         print("Adivinaste, mi número era", d)
       elif d!=x:
         e=int(input("Inténtalo de nuevo, ingresa otro número: ")
         if e==x:
           print("Adivinaste, mi número era", e)
         else:
           print("No adivinaste, mi número era", x)
      
    