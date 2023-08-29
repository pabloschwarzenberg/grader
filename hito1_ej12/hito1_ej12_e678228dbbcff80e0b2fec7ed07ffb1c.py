#Juego adivina mi número
import random
numero=random.randrange(1,20)
num=int(input("ingrese primera respuesta"))
if(num==numero):
    print("Adivinaste, mi número era",numero)
else:
    if(num>numero):
     print("mi numero es menor")
    if(num<numero):
     print("mi numero es mayor")
    num=int(input("ingrese segunda respuesta"))
    if (num == numero):
        print("Adivinaste, mi número era",numero)

    else:
        if (num > numero):
         print("mi numero es menor")
        if (num < numero):
         print("mi numero es mayor")
        num=(int(input("ingrese tercera respuesta")))
        if (num == numero):
            print("Adivinaste, mi número era",numero)

        else:
            if (num > numero):
                print("mi numero es menor")
            if (num < numero):
                print("mi numero es mayor")
            num=(int(input("ingrese cuarta respuesta")))
            if (num == numero):
                print("Adivinaste, mi número era", numero)
            else:
                if (num > numero):
                 print("mi numero es menor")
                if (num < numero):
                 print("mi numero es mayor")
                 num = (int(input("ingrese quinta respuesta")))
                if (num == numero):
                 print("Adivinaste, mi número era", numero)
                else:
                    print("No adivinaste, mi número era", numero)      