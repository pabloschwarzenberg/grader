

def genomas(string):
    for c in string:
        if c == ["A", "a", "c", "C", "t", "T", "g", "G"]:
            print("Secuencia correcta")
        else: 
            print("Secuencia incorrecta")

mensaje = input("Ingrese una secuencia de ADN: ")

genomas(mensaje)
