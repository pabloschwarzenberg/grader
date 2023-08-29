#Descomponer un número
A= int(input("ingrese un numero"))

if A>0:
    mi = A//1000
    cen = ( A%1000)//100
    de = ((A%1000)%100)//10
    uni = ((A%1000)%100)%10
    print(str(mi) + "m+" + str(cen) + "c+" + str(de) + "d+" + str(uni) + "u")
else:
    print("el numero escrito debe ser de maximo 4 digitos")
      