def numero_perfecto(numero):
      suma_divisores = 0
      for i in range(1,numero):
           if numero % i == 0:
           suma_divisores +=1
      return  suma_divisores == numero     
    
int(input('ingrese numero'))
if es_numero_perfecto(numero):
  print('el numero es ',numero 'es perfecto')
  
else:
    print('el numero ',numero 'no perfecto')

