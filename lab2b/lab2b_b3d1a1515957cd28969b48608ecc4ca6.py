#multiplos
A=int(input("ingrese primer número: "))
Z=int(input("ingrese segundo número: "))
intentos=A
while A<=Z:
   if A%2==0 or A%7==0:
      print(A)
   A=A+1 