def numero_perfecto(a):
    divisores=[]
    numero= range(a)
    lista_numero= list(numero)
    lista_numero.remove(0)
    for numerillo in lista_numero:
       resto=a%numerillo
       if resto==0:
          divisores.append(numerillo)
       else:
          pass
    suma=0
    for numerito in divisores:
       suma=suma+numerito
    if suma==a:
       return True
    else:
       return False
           