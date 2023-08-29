#Contestador de celular
n_telefono = int(input("Ingrese un número telefonico: "))
n_hora = int(input("Ingrese la hora de la llamada: "))
ultimos_3_números = (n_telefono%1000)
primeros_3_números =(n_telefono//100000)

if n_hora >= 0 and n_hora <= 7:
        print("Contestar")
else:
    if n_hora < 14 and ultimos_3_números != 909 :
            print("No contestar")
    elif n_hora >= 0 and n_hora < 14 and ultimos_3_números == 909:
        print("Contestar")
    else:
        if n_hora >= 17 and n_hora <= 19 and  primeros_3_números != 877:
                print("Contestar")
        else:
            print("No contestar")

