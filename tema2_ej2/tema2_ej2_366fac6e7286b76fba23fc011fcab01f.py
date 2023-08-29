def amigos(a,b):
    if a==b:
      return False
    lista=[a,b] 
    divisores_a= [x for x in range(1,a+1) if a%x==0]
    divisores_b= [x for x in range(1,b+1) if b%x==0]
    suma_a= 0
    suma_b=0
    for i in divisores_a:
        suma_a+=i
    for i in divisores_b:
        suma_b+=i
    if suma_a == suma_b:
        return True
    else:
        return False
           