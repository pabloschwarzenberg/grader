#Contestador de celular

n_celular = int(input("Ingrese el Número telefónico: "))
hora = int(input("Ingrese la hora de la llamada: "))
n_celular = str(n_celular)
termino = n_celular[5:8]  


if hora > 0 and hora <= 7:
    print("Contestar")

elif hora < 14:
    if termino == "909":
        print("Contestar")
    else:
        print("No contestar")

elif hora >= 17 and hora <= 19:
    if termino != "877":
        print("No contestar")
    else:
        print("Contestar")

elif hora > 19:
    print("No contestar")

