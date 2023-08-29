numero = eval(input("Ingrese numero decimal: "))
codigo = ""
while(not(numero == 0)):
    numero = (numero/2)
    
    if(numero == int(numero)):
        par = "0"
        codigo = codigo + par
        numero = int(numero)
        
        if(numero == 1):
            numero = 0
            codigo = codigo + impar
        

    else:
        impar = "1"
        codigo = codigo + impar
        numero = int(numero)
        if(numero == 1):
            numero = 0
            codigo = codigo + impar

print("resultado =",(codigo)[::-1])