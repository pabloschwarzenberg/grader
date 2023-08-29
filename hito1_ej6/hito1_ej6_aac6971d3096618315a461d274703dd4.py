numero1 = eval(input("ingrese el primer numero  "))
numero2 = eval(input("ingrese el segundo numero  "))
numero3 = eval(input("ingrese el tercer numero  "))
if (numero1<=numero2<=numero3):
  print("{} , {} , {}".format(numero1 , numero2 , numero3))
else:
    if(numero2 <= numero3 <= numero1):
        print("{} , {} , {}".format(numero2 , numero3 , numero1))
    else:
        if(numero3 <= numero2 <= numero1):
            print("{} , {} , {}".format(numero3 , numero2 , numero1))
        else:
            if(numero3 <= numero1 <= numero2):
                print("{} , {} , {}".format(numero3 , numero1 , numero2))
            else:
                if(numero1 <= numero3 <= numero2):
                    print("{} , {} , {}".format(numero1 , numero3 , numero2))
                else:
                    if(numero2 <= numero1 <= numero3):
                        print("{} , {} , {}".format(numero2 , numero1 , numero3))
                
                   
                        