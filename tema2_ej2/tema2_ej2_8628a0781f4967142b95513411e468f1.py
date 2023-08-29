# completa el código de la función
def numeros_amigos(a,b):
    suma_a =0
    suma_b =0
    for i in range(1,a):
        if a%i==0:
            suma_a+=i
 
    for k in range(1,b):
        if b%k==0:
            suma_b+=k
 
    return suma_a==b and suma_b==a

  numero_1 = int()
  numero_2 = int()
 
  if numeros_amigos(numero_1,numero_2):
      print ("True")
  else:
      print ("False")