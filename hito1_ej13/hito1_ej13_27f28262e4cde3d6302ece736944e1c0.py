#Factores Primos
num=eval(input("ingrese un valor:"))
if num>0:
    for i in range(2,num):
        esPrimo= True
        n=2
        while esPrimo and n<i:
            if i% n== 0:
                print(i)
            else:
                n+=1
        

