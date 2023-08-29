#Descomponer un número
x= int(input("ingrese un numero de 4 digitos"))
if 10000>x>999:
    milesima= x//1000
    centena= ((x-(milesima*1000))//100)
    decena= ((x-(milesima*1000+(centena*100)))//10)
    unidad= (x-(milesima*1000+(centena*100)+(decena*10)))
    print(milesima,"M +",centena,"C +",decena,"D +",unidad,"U")
else:
    if 1000>x>99:
          centena= (x//100)
          decena= ((x-(centena*100))//10)
          unidad= (x-((centena*100)+(decena*10)))
          print(centena,"C +",decena,"D +",unidad,"U")
    else:
        if 100>x>9:
            decena= (x//10)
            unidad= (x-(decena*10))
            print(decena,"D +",unidad,"U")
        else:
            if 10>x:
                print(x,"U")
                
        