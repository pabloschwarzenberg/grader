#Gustavo Altez Irarrazabal
Numero1=int(input("Ingrese primer Numero: " ))
Numero2=int(input("Ingrese segundo Numero: " ))
Numero3=int(input("Ingrese Tercer Numero: " ))
if Numero1<Numero2<Numero3:
  print(Numero1,",", Numero2,",", Numero3)
if Numero1>Numero2>Numero3:
  print(Numero3,",", Numero2,",", Numero1)
if Numero1<Numero3<Numero2:
  print(Numero1,",", Numero3,",", Numero2)
if Numero2<Numero1<Numero3:
  print(Numero2,",", Numero1,",", Numero3)
if Numero2<Numero3<Numero1:
  print (Numero2,",", Numero3,",", Numero1)
if Numero3<Numero1<Numero2:
  print (Numero3,",", Numero1,",", Numero2)
if Numero1==Numero2==Numero3:
  print(Numero1,",", Numero2,",", Numero3)
if Numero1==Numero2 and Numero2>Numero3:
  print(Numero3,",", Numero2,",", Numero1)
if Numero1>Numero2 and Numero2==Numero3:
    print(Numero2,",", Numero3,",", Numero1)
if Numero1==Numero2 and Numero2<Numero3:
  print(Numero1,",", Numero2,",", Numero3)
if Numero2==Numero3 and Numero3<Numero1:
  print(Numero2,",", Numero3,",", Numero1)
if Numero1==Numero3 and Numero1>Numero2:
  print(Numero2,",", Numero3,",", Numero1)
if Numero2>Numero1 and Numero1==Numero3:
  print(Numero1,",", Numero3,",", Numero2)