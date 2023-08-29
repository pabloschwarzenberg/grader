# completa el código de la función
def amigos(a,b):    
    indice = 1
    suma = 0
    bandera = False
    while indice < a:       
        if(a % indice == 0):
          suma = suma + indice         
        indice = indice + 1   
    if(suma == b):
         print("los numeros son amigos")
         bandera = True
    else:
         print("los numeros no son amigos")
         bandera = False
      
    return bandera

try:
    primero = int(input("Ingrese el primer numero :"))
    segundo = int(input("Ingrese el segundo numero :"))
    print(amigos(primero,segundo))
except:
    pass 
           