#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.

numero1 = int(input("Introduzca el primer valor: "))
numero2 = int(input("Introduzca el segundo valor: "))
numero3 = int(input("Introduzca el tercer valor : "))

if 3 == 3:
    #123
    if (numero1 < numero2)and (numero1 < numero3)and (numero2 < numero3):
        print (numero1,numero2,numero3)
    #132
    elif (numero1 < numero2)and (numero1 < numero3)and (numero2 > numero3):
        print (numero1,numero3,numero2)
    #213
    elif (numero1 > numero2)and (numero1 < numero3)and (numero2 < numero3):
        print (numero2,numero1,numero3)
    #231  
    elif (numero1 > numero2)and (numero1 > numero3)and (numero2 < numero3):
        print (numero2,numero3,numero1)
    #312
    elif (numero1 < numero2)and (numero1 > numero3)and (numero2 > numero3):
        print (numero3,numero1,numero2)
    #321
    elif (numero1 > numero2)and (numero1 > numero3)and (numero2 > numero3):
        print (numero3,numero2,numero1)
        
    elif (numero1 == numero2) or (numero1 == numero3) or (numero2 == numero3):

        if (numero1==numero2)and (numero3 > numero1):
            print (numero1,numero2,numero3)
            
        elif (numero1==numero2)and (numero3 < numero1):
            print (numero3,numero2,numero1)
            
        elif (numero1==numero3)and(numero2 > numero1):
            print (numero1,numero3,numero2)
            
        elif (numero1==numero3)and(numero2 < numero1):
            print (numero2,numero1,numero3)
            
        elif (numero2==numero3)and(numero1 > numero2):
            print (numero2,numero3,numero1)
            
        elif (numero2==numero3)and(numero1 < numero2):
            print (numero1,numero2,numero3)