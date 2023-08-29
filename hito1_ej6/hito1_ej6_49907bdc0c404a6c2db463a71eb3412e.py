#Ordenar tres números
numero=int(input("ingrese un numero"))
numero2=int(input("ingrese un numero"))
numero3=int(input("ingrese un numero"))
if(numero<numero2<numero3):
    print(numero, "," ,numero2,",", numero3)
elif(numero2<=numero3<=numero):
    print(numero2,",", numero3,",", numero)
elif(numero3<=numero<=numero2):
    print(numero3,",", numero ,",", numero2)
elif(numero2<=numero<=numero3):
    print(numero2 ,",", numero,",", numero3)
elif(numero3<=numero2<=numero):
    print(numero3 ,"," ,numero2,",", numero)
elif(numero<=numero2<=numero3):
    print(numero,",", numero2,",", numero3)