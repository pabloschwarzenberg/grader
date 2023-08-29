def numero_perfecto(a):
 contador1=0
 contador2=0
 suma=0
 
 i=1
 for j in range(2,a):
     
   contador1=0
   i=1
   while i<j:
    if j%i==0:
       contador1 = contador1 + i
    i=i+1   

   if contador1==j:
     suma=suma+j
     global suma

 while i<a:
    if a%i==0:
        contador1 = contador1 + i
    i=i+1   

 if contador1==a:
     return True
 else: return False
if __name__=="__main__":
    a=int(input('Ingrese el número: '))
    f=numero_perfecto(a)
    print('El número es perfecto ?:', numero_perfecto(a))
    print('La suma de los [n] números perfectos antes del elegido es:',suma)