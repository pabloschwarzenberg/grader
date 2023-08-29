numero1= int(input("ingresar primer numero:"))
numero2= int(input("ingresar segundo numero:"))
numero3= int(input("ingresar tercer numero:"))

if (numero1>=numero2) and (numero1>=numero3) and (numero2>=numero3):
    print (numero3,(","),numero2,(","),numero1,)
if (numero1>=numero2) and (numero1>=numero3) and (numero2<=numero3):
        print(numero2,(","),numero3,(","),numero1,)
else:
    if(numero1<=numero2) and (numero2>=numero3) and (numero1<=numero3):
            print (numero1,(","),numero3,(","),numero2,)
    elif (numero1<=numero2) and (numero2>=numero3) and (numero1>=numero3):
        print (numer3,(","),numero1,(","),numero2,)
    else:
        if(numero1<=numero3) and (numero3>=numero2) and (numero1>=numero2):
                print (numero2,(","),numero1,(","),numero3,)
        elif (numero1<=numero3) and (numero3>=numero2) and (numero1<=numero2):
                print (numero1,(","),numero2,(","),numero3,)