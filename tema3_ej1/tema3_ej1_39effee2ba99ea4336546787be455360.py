# completa el código de la función
def suma_divisores(a):
   
    divisores=[1]
    resultado=0
    for i in range(2,a+1):
        if a%i==0:
            divisores.append(i)
        
    for i in divisores:
        resultado+=i

    resultado-=a
    if resultado==1:
        return resultado,True
    else:
        return resultado,False

if __name__ == "__main__": 
  suma_divisores(a)
    
