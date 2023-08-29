#Descomponer un número
numero=eval(input("ingrese un numero "))
if(numero>0 and numero<=9999):
  formula1=numero//1000
  formula2=numero//100%10
  formula3=numero//10%10
  formula4=numero//1%10
  print(formula1,"M","+",formula2,"C","+",formula3,"D","+",formula4,"U")  