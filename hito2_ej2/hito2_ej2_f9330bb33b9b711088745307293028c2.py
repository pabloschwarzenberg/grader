def Revisar(palabra):
    Contador= 0
    Letras = ["A","C","T","G","a","c","t","g"]
    for i in palabra:
        if i not in Letras:
            Contador = 1
    if Contador == 1:
        print("Secuencia Incorrecta")
    else:
        print("Secuencia Correcta")
    return


palabra = input("\nIngresar palabra a analizar :" )
Revisar(palabra)      