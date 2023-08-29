#Ordenar 3 numeros
while 1: 
    try: #Manejo de excepciones
        #Arreglo vacío para guardar los números que ingrese el usuario
        numeros = []
        #ciclo for para capturar los números
        for i in range(3):
            #Pedir al usuario ingresar los números
            numero= int(input("ingrese 3 número diferentes: ")) 
            #Guardar cada número en el arreglo
            numeros.append(numero)
        #ordenar los números al salir del bucle 
        ordenados = sorted(numeros) 
        #Imprimir el resultado si todo funciona bien
        print(ordenados[0],",", ordenados[1],",",ordenados[2]) 



 