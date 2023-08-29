def ordenar_numeros(numero_x1, numero_x2, numero_x3):
   
    num_menor = min(numero_x1, numero_x2, numero_x3)
    num_mayor = max(numero_x1, numero_x2, numero_x3)
    num_intermedio = (numero_x1 + numero_x2 + numero_x3) - num_menor - num_mayor

 
    print(num_menor, num_intermedio, num_mayor,sep=",")
    
numero1 = int(input("ingresa el primer número: "))
numero2 = int(input("ingresa el segundo número: "))
numero3 = int(input("ingresa el tercer número: "))

ordenar_numeros(numero1, numero2, numero3)
