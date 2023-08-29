print("Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor")
numero_1 = int(input("numero entero 1: "))
numero_2 = int(input("numero entero 2: "))
numero_3 = int(input("numero entero 3: "))
 
print("mi primer numero entero es: ", numero_1 ,)
print("mi segundo numero entero es: ", numero_2 ,)
print("mi tercer numero entero es: ", numero_3 ,)

if numero_1 <= numero_2 and numero_1 <= numero_3:
    print("el numero 1 que es:", numero_1 , "es menor que numero 2 que es:", numero_2 , ",y numero 3 que es:", numero_3,)
    if numero_2 >= numero_3:
        print("mientras que el numero 1 es el menor, el numero 3 seria el medio y el numero 2 seria el mayor de todos")
    else:
        print("mientras que el numero 1 es el menor, el numero 2 es el medio y el numero 3 es el mayor")
    print("este seria el primer caso, si es que el numero 1 fuera siempre el menor de todos")
elif numero_3 <= numero_1 and numero_3 <= numero_2:
    print("en este caso el numero 3 seria el menor de todos y se debe evaluar si el numero 1 o el numero 2 sera el mayor o no")
    if numero_1 >= numero_2:
        print("mientras que el numero 3 es el menor de todos, el numero 1 es el mayor de todos, y el numero 2 sera el medio")
    else:
        print("mientras que el numero 3 es el menor de todos, el numero 2 es el mayor de todos, y el numero 1 sera el medio")
    print("este seria el segundo caso, si es que el numero 3 fuera siempre el menor de todos")
elif numero_2 <= numero_1 and numero_2 <= numero_3:
    print("el numero 2 sera el menor de todos, se decidira si el numero 1 o el numero 3 sera el mayor")
    if numero_3 >= numero_1:
        print("el numero 3 sera el mayor, y el numero 1 sera el medio")
    else:
        print("el numero 1 sera el mayor, y el numero 3 sera el medio")
    print("este seria el tercer caso si el numero 2 fuera el menor de todos")
    max = max(numero_1, numero_2, numero_3)
    min = min(numero_1, numero_2, numero_3)
    med = (numero_1 + numero_2 + numero_3) - max - min
    print("el orden de menor a mayor, en orden creciente es: ", min, ",", med, ",", max,)