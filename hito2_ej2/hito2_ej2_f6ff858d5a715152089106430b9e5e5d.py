# contiene solamente las letras A,C,T,G

def genoma(secuencia):
    nucleotidos = ["A", "C", "T", "G"]
    secuencia = secuencia.upper()
    verificador = 0

    for i in secuencia:
        if i in nucleotidos:
            verificador = verificador + 0
            
        else:
            verificador += 1
    
    if verificador == 0:
        return True
    else:
        return False

#Programa

secuencia = input("Ingrese secuencia ADN: ")
validacion = genoma(secuencia)

if validacion == True:
    print("Secuencia correcta")

else:
    print("Secuencia incorrecta")