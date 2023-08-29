def numero_perfecto(numero):
    x=1
    suma=0
    while x != numero:
        
        if numero%x == 0:
            
            suma = suma+x
            
        x = x+1
        
    if suma==numero:
        
        return True
    
    else:
        return False


if __name__ == "__main__":
    
    numero = int(input("Ingrese su numero: "))
    
    if numero_perfecto(numero):
        print("El numero",numero,"es perfecto")
    else:
        print("El numero", numero,"no es perfecto")
