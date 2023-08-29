#Descomponer un número
unidades = ["U","D","C","M"]

numero = input("ingrese numero: ")
largo = len(numero)
while largo != 0 :
    for caracteres in numero:
        print(caracteres + unidades[largo-1],end="")
        
        largo -=1
        if largo != 0:
            print("+", end="")
        if largo == 0:
            a = 1
        
        
        