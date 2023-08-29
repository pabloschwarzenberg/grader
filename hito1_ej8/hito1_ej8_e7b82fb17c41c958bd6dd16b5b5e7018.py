#Descomponer un número
numero=int(input("ingrese un numero de hasta 4 digitos: "))
if(numero>0 and numero<99):
    descomposicion=numero//10
    resto=numero%10
    print(descomposicion,"D +" ,resto,"U")
elif(numero>=100 and numero<1000):
    descomposicion=numero//100
    resto=numero%100
    descomposicion2=resto//10
    resto2=resto%10
    print(descomposicion,"C +",descomposicion2,"D +",resto2,"U")
elif(numero>=1000 and numero<10000):
    descomposicion=numero//1000
    resto=numero%1000
    descomposicion2=resto//100
    resto2=resto%100
    descomposicion3=resto2//10
    resto3=resto2%10
    print(descomposicion,"M +",descomposicion2,"C +",descomposicion3,"D +",resto3,"U") 
   