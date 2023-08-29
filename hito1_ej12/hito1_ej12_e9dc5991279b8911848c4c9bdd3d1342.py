#Juego adivina mi número
ciclo=0
ciclo1=0
contador=0
n=random.randint(1,20)

while(ciclo==0):
    print("Adivina el numero del 1 al 20 ")
    while(ciclo1==0):
        i=int(input("\nnumero: "))
        if numero==n:
            ciclo1=1
            ciclo=1
            print(f"Adivinaste, mi número era {n}")
        else:
            contador=contador+1
            if i>n:
                print("mi numero es menor")
            else:
                print("mi numero es mayor")
        if contador==5:
            ciclo1=1
            ciclo=1
            print(f"No adivinaste, mi número era {n}")