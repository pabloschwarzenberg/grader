#Descomponer un número
N=int(input("Ingresar numero de 1 a 4 digitos: "))

if 1000 <= N:

  Duno=int(N/1000)
  Ddos=int(N/100)%10
  Dtres=int(N/10)%10
  Dcuatro=N%10
  
  print(Duno,"M+",Ddos,"C+",Dtres,"D+",Dcuatro,"U")

if 100 <= N <=999:

  DDuno=int(N/100)
  DDdos=int(N/10)%10
  DDtres=N%10
  
  print(DDuno,"C+",DDdos,"D+",DDtres,"U")

if 10 <= N <= 99:

  DDDuno=int(N/10)
  DDDdos=N%10
  
  print(DDDuno,"D+",DDDdos,"U")

if 1 <= N <= 9:

  DDDDuno=N
  
  print(N,"U")
