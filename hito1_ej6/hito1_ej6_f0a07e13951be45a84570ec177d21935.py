#Ordenar tres números
numero1=eval(input("ingrese numero"))
numero2=eval(input("ingrese numero"))
numero3=eval(input("ingrese numero"))

if numero1<=numero2<=numero3:
  print (numero1, ",", numero2, ",", numero3)
elif numero2<=numero1<=numero3:
    print (numero2, "," ,numero1, ",", numero3)
elif numero3<=numero1<=numero2:
  print (numero3, ",",numero1,",",numero2)
elif numero3<=numero2<=numero1:
  print(numero3, "," ,numero2, "," ,numero1)