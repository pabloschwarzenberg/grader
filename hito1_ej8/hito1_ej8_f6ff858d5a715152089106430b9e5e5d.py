#Descomponer un número

print("Ahora haremos la descomposicion de un numero de 4 digitos")
numero = eval(input("Ingrese numero de hasta 4 digitos: "))

if 4 == len(str(numero)):
    
    unidades = numero%10
    numero = numero//10
    
    decenas = numero%10
    numero = numero//10
    
    centenas = numero%10
    numero = numero//10
    
    unidadesMil = numero%10

    frase1 = "U"
    frase2 = "D"
    frase3 = "C"
    frase4 = "M"
    frase5 = "+"
    
    frase = str(unidadesMil) + "" + frase4 + "" + frase5 + "" + str(centenas) + "" + frase3 + "" + frase5 + "" + str(decenas) + "" + frase2 + "" + frase5 + "" + str(unidades) + "" + frase1
     
    print(frase)

elif 3 == len(str(numero)):
    
    unidades = numero%10
    numero = numero//10

    decenas = numero%10
    numero = numero//10

    centenas = numero%10
    
    frase1 = "U"
    frase2 = "D"
    frase3 = "C"
    frase5 = "+"
    
    frase = str(centenas) + "" + frase3 + "" + frase5 + "" + str(decenas) + "" + frase2 + "" + frase5 + "" + str(unidades) + "" + frase1

    
    print(frase)

elif 2 == len(str(numero)):
    
    unidades = numero%10
    numero = numero//10

    decenas = numero%10
    numero = numero//10

    frase1 = "U"
    frase2 = "D"
    frase5 = "+"
    
    frase = str(decenas) + "" + frase2 + "" + frase5 + "" + str(unidades) + "" + frase1
    
    print(frase)

elif 1 == len(str(numero)):
    
    unidades = numero%10
    numero = numero//10

    frase1 = "U"
    frase = str(decenas) + "" + frase2
    
    print(frase)

else:
    print("ERROR")
