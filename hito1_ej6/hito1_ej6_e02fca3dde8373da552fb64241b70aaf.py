def ordenar_numeros():

    numero1 = int(input("Introduce el primer número: "))
    numero2 = int(input("Introduce el segundo número: "))
    numero3 = int(input("Introduce el tercer número: "))

  
    lista_numeros = [numero1, numero2, numero3]

   
    lista_numeros.sort()


    print(f'{lista_numeros[0]}, {lista_numeros[1]}, {lista_numeros[2]}')

ordenar_numeros()