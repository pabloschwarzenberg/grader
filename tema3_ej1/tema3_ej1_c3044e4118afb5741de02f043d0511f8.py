# completa el código de la función
def suma_divisores(a):
    divisores = [1]
    
    for i in range(2, a + 1):
        #print(i, "uno")
        if (a % i == 0) and (i != a):
            divisores.append(i) 
        #print(i, "dos")
        
    #print(i, "tres")
    #divisores.pop(i)
    suma = sum(divisores)
    b = True
    for i in range(2, a):
        #print("entro 1")
        #print(a, i)
        if a % i == 0:
            #print("entro 2")
            b = False
            break   
    
    #for i in range(2, a):
        #print(i,"aqui")
        #if a % i == 0:
            #print("No es primo", a, "es divisor")
            #b = False
            #return (a,False)
    #print("Es primo")
    
    if a == 1:
        #return #(a,False)
        b = False
        suma = 0
    #if a != 1:
     #   suma = sum(divisores)
        #b = True
        
    #b = True #return #(a,True)
    
    
    return (suma,b)
   
    
if __name__ == "__main__":
    #main()
    
    resultado = suma_divisores(a)
    #resultado = resultado - a
    print(resultado)
    
    #resultado2 = es_primo(a,b)
    #print(resultado2)
    
    
    #print(divisores,b)
    