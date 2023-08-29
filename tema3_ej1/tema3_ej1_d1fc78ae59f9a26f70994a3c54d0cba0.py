# completa el código de la función
def suma_divisores(a):
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
    cantidad_divisores=len(divisores)+1
    
    if cantidad_divisores==2:
       return suma,True
    else:
       return suma,False
           

           