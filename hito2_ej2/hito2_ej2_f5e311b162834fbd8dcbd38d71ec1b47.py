def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra.lower() in "actg":
            print("secuencia incorrecta")
            return False
            
    print("secuencia correcta")      
    return True
secuencia = input("ingrese la secuencia")
print("¿Es válida?")
print(secuencia_valida(secuencia)) 
    