# por favor escribe aquí tu función
numero = int()

def es_primo(num):
    contador=0
    for i in range(1,num+1):
        if num % i == 0:
         contador += 1
         
    if contador == 2:
        return True
        
    else:
        return False
        

resultado = (es_primo(numero))
print(resultado)

        

resultado = (es_primo(numero))
print(resultado)
