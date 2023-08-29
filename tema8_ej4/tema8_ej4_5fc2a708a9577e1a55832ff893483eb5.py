def rot13(palabra):
    alfabeto="abcdefghijklmnopqrstuvwxyz"
    palabra2=""
    for i in palabra:
        rot13=alfabeto.find(str(i))+13
        if rot13>25:
            rot13=alfabeto.find(str(i))-13
        palabra2+=alfabeto[rot13]
    return palabra2
if __name__=="__main__":
    palabra=input("Ingresa la palabra que quieras encriptar: ")
    palabra.lower()
    resultado=rot13(palabra)
    print("El resultado es: ",resultado)