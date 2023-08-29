# completa el código de la función
a=int()
b=int()

suma1 = 0
suma2 = 0
for i in range(1,a):
   if a % i == 0:
     suma1+=i
 
for k in range(1,b):
    if b % k == 0:
     suma2 += k
if suma1 == b and suma2 == a:
    
        print(True)
else:
    print(False)
