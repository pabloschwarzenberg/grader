genoma=input("ingresa la secuencia:")
def validar(secuencia):
    lista_letras=["A","C","T","G"]
    letras="ACTG"
    secuencia.upper()
    contador=0
    for i in secuencia:
        validador=letras.find(i)
        contador+=1
        if validador==-1:
            print("secuencia incorrecta")
        elif contador==(len(secuencia)):
            print("secuencia correcta")
validar(genoma)            
