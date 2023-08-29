# completa el código de la función
def suma_divisores(numero):
    suma=0
    primo=1
    for div in range(1, numero):
        if numero % div== 0:
           suma= suma+div
           print(suma)
    if primo == suma:
         primo= True 
    else:
        primo= False
             
    return suma,primo
  
  
           