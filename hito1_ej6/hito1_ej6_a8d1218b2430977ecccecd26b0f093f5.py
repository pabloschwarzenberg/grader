#Ordenar tres números
def numeros(num1,num2,num3):
     #Calcular el menor
    menor = num1
    if num2 < menor:
        menor = num2
    elif num3 < menor:
        menor = num3

    #Calcular el mayor
    mayor = num1
    if num2 > mayor:
        mayor = num2
    elif num3 > mayor:
        mayor = num3
     
     #Calcular el del medio
    medio = num1 + num2 + num3 - menor - mayor

    #Resultado
    print(f"{menor}, {medio}, {mayor}")
    


uno = int(input("Primer número: "))
dos = int(input("Segundo número: "))
tres = int(input("Tercer número: "))

numeros(uno,dos,tres)