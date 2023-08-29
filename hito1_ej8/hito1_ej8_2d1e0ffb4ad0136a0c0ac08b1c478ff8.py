#Descomponer un número
numero = str(input())

largo = len(numero)

while(largo > 4) or (largo < 0):
    print("escriba otro numero")
    numero = str(input())

if(largo == 1):
    print("U:", numero)

else:
    if(largo == 2):
        print(numero[0],"D","+",numero[1],"U")
    else:
        if(largo == 3):
            print(numero[0],"C","+",numero[1],"D","+",numero[2],"U")
        else:
            if(largo == 4):
                print(numero[0],"M","+",numero[1],"C","+",numero[2],"D","+",numero[3],"U")
     