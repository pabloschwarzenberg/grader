def numero_perfecto(a):
    #recibimos como parametro solo el numero a, al cual queremos obtener sus divisores
    divisor=1
    divisores=[]
    while divisor<a :
        resto=a%divisor
        if resto==0 :
            divisores.append(divisor)
        divisor=divisor+1
    suma=0
    for i in divisores:
        suma=suma+i
    print(suma)
    if len(divisores)==1:
        primo=1
    else:
        primo=0
        
    if a==suma:
      return True
    else:
      return False