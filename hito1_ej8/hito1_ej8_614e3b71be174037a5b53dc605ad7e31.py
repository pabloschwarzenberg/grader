#Descomponer un número
numero=0
while (numero<=1 or numero>=9999):
  numero=int(input("Numero de 1 a 4 digitos: "))
  
  if (numero>=1000 and numero<=9999):
    a1=numero//1000
    a2=(numero%1000)//100
    a3=(numero%100)//10
    a4=numero%10
    print("",a1,"M +",a2,"C +",a3,"D +",a4,"U")
  
  elif (numero>=100 and numero<=999):
    b1=numero//100
    b2=numero%100//10
    b3=numero%10
    print("",b1,"C +",b2,"D +",b3,"U")

  elif (numero>=10 and numero<=99):
    c1=numero//10
    c2=numero%10
    print("",c1,"D +",c2,"U")

  elif (numero>=1 and numero<=9):
    d1=numero
    print("",d1,"U")