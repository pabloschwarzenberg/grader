def jerigonzo(string):
    lista = list(string)
    print("lista",lista[1])
    lista2 = ["a","e","i","o","u"]
    lista3 = []
    print("lista2",lista2[0])
    for i in range(len(lista)):
        if(lista2[0] == lista[i]):
            lista3.append("a")
            lista3.append("p")
            lista3.append("a")
        elif(lista2[1] == lista[i]):
            lista3.append("e")
            lista3.append("p")
            lista3.append("e")
        elif(lista2[2] == lista[i]):
            lista3.append("i")
            lista3.append("p")
            lista3.append("i")
        elif(lista2[3] == lista[i]):
            lista3.append("o")
            lista3.append("p")
            lista3.append("o")
        elif(lista2[4] == lista[i]):
            lista3.append("u")
            lista3.append("p")
            lista3.append("u")
        else:
            lista3.append(lista[i])
    string = "".join(lista3)
    return string

if __name__ == "__main__":
    string = input("Ingrese un texto")
    string = jerigonzo(string)
         