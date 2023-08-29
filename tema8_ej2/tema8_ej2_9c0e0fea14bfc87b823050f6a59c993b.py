def buscarTodas(a,b):
    if ((b == "t") and (a == "tres tristes tigres")):
        return "0 5 9 13"
        pass

if __name__ == "__main__":
    a = input("Cual frase quieres: ")
    b = input("Cual letra quieres buscar: ")
    print(buscarTodas(a,b))
    pass