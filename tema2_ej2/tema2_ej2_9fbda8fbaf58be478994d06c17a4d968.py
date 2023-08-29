# completa el código de la función
def amigos(a,b): 
  DV1=1 
  DV2=1 
  SV1=0 
  SV2=0 
  while DV1<a: 
    if a%DV1==0: 
      SV1+=DV1 
      print("divisor de %d es: %d" % (a,DV1),"la suma de divisores de %d es: %d" %(a,SV1)) 
    DV1+=1 
  while DV2<b: 
    if b%DV2==0: 
      SV2+=DV2
      print("divisor de %d es: %d" % (b,DV2),"la suma de divisores de %d es: %d" %(b,SV2)) 
    DV2 += 1 
  if SV1==b and SV2==a: 
    return True 
  else: 
    return False 
try: 
 N1 = int(input("Ingrese primer numero: ")) 
 N2 = int(input("Ingrese segundo numero: ")) 
 print(amigos(N1,N2)) 
except: 
 print("Por favor, ingresar numeros")