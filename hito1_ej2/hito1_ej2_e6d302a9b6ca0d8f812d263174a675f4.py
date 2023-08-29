#Contestador de celular
numt= int(input("Ingrese numero telefonico: "))
hr= int(input("Ingrese hora de la llamada: "))
n=numt
n1= n%1000
n2= n//100000
if ((hr==range(0,7)) or ((hr<=14)and(n1==909)) or ((hr==range(17,19))and(n2!=877))):
  print("Resultado: CONTESTAR")
elif (((hr>=14)and(n1!=909)) or (hr>=19)):
  print("Resultado: NO CONTESTAR") 