def secuencia_valida(secuencia):
        for letra in secuencia:
            if not letra.lower() in "actg":
                print ("secuencia incorrecta")        
        print("secuencia correcta")
        
x = input("ingrese string: ")
print (secuencia_valida(x))      