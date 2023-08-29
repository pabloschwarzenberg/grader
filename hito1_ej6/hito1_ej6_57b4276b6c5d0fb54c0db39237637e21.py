#Ordenar tres números

numero1 = int(input("ingrese primer número: "))
numero2 = int(input("ingrese segundo número: "))
numero3 = int(input("ingrese tercer número: "))

imprimir1 = 0;
imprimir2 = 0;
imprimir3 = 0;

if numero1 < numero2:
    if numero1 < numero3:
        imprimir1 = numero1
        if numero2 < numero3:
            imprimir2 = numero2
            imprimir3 = numero3
        else:
            imprimir2 = numero3
            imprimir3 = numero2
    else:
        imprimir1 = numero3
        imprimir2 = numero1
        imprimir3 = numero2
else:
    if numero1 < numero3:
        imprimir1 = numero2
        imprimir2 = numero1
        imprimir3 = numero3
    else:
        imprimir3 = numero1
        if numero2 < numero3:
            imprimir1 = numero2
            imprimir2 = numero3
        else:
            imprimir1 = numero3
            imprimir2 = numero2

print(imprimir1, "," , imprimir2, ",", imprimir3 )


