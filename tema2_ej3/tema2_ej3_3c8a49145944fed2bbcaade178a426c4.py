def numero_perfecto(numero):
    if numero <= 0:
        print("No puedo calcular los divisores de un numero menor o igual a cero.")
    else:
        suma= 0
        lista= []
        print("Los divisores de", numero, "son ", end="")
        for i in range(1, numero):
            if numero % i == 0:
                print(i, end=" ")
                suma= suma+i
                lista.append(i)
    if suma==numero:
        print(", por lo tanto "+str(numero)+" es perfecto.")
        return True   #NO RETURNA TRUE
    else:
        print(", por lo que "+str(numero)+" no es perfecto.")
        return False

if __name__=="__main__":
    numero = int(input("Escriba un número que quiera comprobar si es perfecto: "))
    perfecto(numero)
           