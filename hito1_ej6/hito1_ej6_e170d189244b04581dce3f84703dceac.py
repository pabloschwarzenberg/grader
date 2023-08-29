#Ordenar tres números
numero1 = int(input(""))
numero2 = int(input(""))
numero3 = int(input(""))

if(numero1 < numero2 and numero2 < numero3):
  print(numero1,",",numero2,",",numero3,sep="")
if(numero1 < numero3 and numero3 <numero2):
   print(numero1,",",numero3,",",numero2,sep="")
if(numero2 < numero1 and numero1 < numero3):
 print(numero2,",",numero1,",",numero3,sep="")
if(numero2 < numero3 and numero3 <numero1):
    print(numero2,",",numero3,",",numero1,sep="")
if(numero3 < numero1 and numero1 < numero2):
 print(numero3,",",numero1,",",numero2,sep="")
if(numero3 < numero2 and numero2 <numero1):
 print(numero3,",",numero2,",",numero1,sep="")
if(numero1 < numero2 and numero2 == numero3):
 print(numero1,",",numero2,",",numero3,sep="")
if(numero1 > numero2 and numero2 == numero3):
 print(numero3,",",numero2,",",numero1,sep="")
if(numero2 < numero1 and numero1 == numero3):
 print(numero2,",",numero1,",",numero3,sep="")
if(numero2 > numero1 and numero1 == numero3):
 print(numero3,",",numero1,",",numero2,sep="")
if(numero3 < numero2 and numero2 == numero1):
 print(numero3,",",numero2,",",numero1,sep="")
if(numero3 > numero2 and numero2 == numero1):
 print(numero1,",",numero2,",",numero3,sep="")