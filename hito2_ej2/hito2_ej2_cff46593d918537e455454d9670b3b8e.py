def adn(n):
    if n == "a":
        return True
    elif n== "c":
        return True
    elif n== "g":
        return True
    elif n=="t":
        return True

    else:
        return False

secuencia = str(input("ingrese secuencia: "))
lista_secuencia = list(secuencia)

valido=(list(map(adn,lista_secuencia)))



print(valido)

variable= False in valido
print(variable)

if variable== True:
    print("secuencia incorrecta")
else:
    print("secuencia correcta")
