#Ordenar tres números
numero1 = int(input("escribe tu primer numero:"))
numero2 = int(input("escribe tu segundo numero:"))
numero3 = int(input("escribe tu tercer numero:"))

if numero1 > numero2:
    if numero2 > numero3:
        print(numero3, ",",numero2,"," , numero1)
    if numero3 > numero2:
        if numero1 > numero3:
            print(numero2, ",",numero3,"," , numero1)
        else:
            print(numero2, ",",numero1,"," , numero3)
else:
        if numero2 > numero3:
            if numero3 > numero1:
                print(numero1, ",",numero3,"," , numero2)
            else:
                print(numero3, ",",numero1,"," , numero2)
        
        if numero3 > numero2:
            print(numero1, ",",numero2,"," , numero3)      