#Descomponer un número
numero=eval(input(''))
if numero>=1000 and numero<=9999:
  numero1=numero//1000
  numero2=(numero//100)%10
  numero3=(numero%100)//10
  numero4=numero%10
  print(numero1,str('M'),'+',numero2,str('C'),'+',numero3,str('D'),'+',numero4,str('U'))
elif numero>=100 and numero<=999:
  numero1=(numero//100)%10
  numero2=(numero%100)//10
  numero3=numero%10
  print(numero1,str('C'),'+',numero2,str('D'),'+',numero3,str('U'))
elif numero>=10 and numero<=99:
  numero1=(numero%100)//10
  numero2=numero%10
  print(numero1,str('D'),'+',numero2,str('U'))
elif numero>1 and numero<9:
  numero1=numero%10
  print(numero1,str('U'))