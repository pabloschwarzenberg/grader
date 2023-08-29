def prueba(cadena, si, no):
    for i in range(len(cadena)):
        if cadena[i] not in si or cadena[i] in no:
            return "secuencia incorrecta"
        
    return "secuencia correcta"
            
    

cadena = input()

cadena = cadena.lower()

no = ['b', 'd', 'e', 'f', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'y', 'z']
si = ['a', 'c', 't', 'g']

print(prueba(cadena, si, no))