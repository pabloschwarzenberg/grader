def es_primo(num):
    contador=0
    for x in range (1,num+1):
        if num%x == 0:
            contador += 1
    if contador == 2:
        return True
    elif contador != 2:
        return False
        
if __name__ == "__main__":
    num = int(input("Ingrese un numero: "))  
    print(es_primo(num))
