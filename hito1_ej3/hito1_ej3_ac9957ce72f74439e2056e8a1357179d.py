#Aprobación de créditos
I = int(input("Income: "))
birthY = int(input("Birth Year: "))
child = int(input("How many children: "))
bankYearsAmount = int(input("How many years have you been with this bank: "))
civilS = input("(S)ingle or (C)Married: ")
urbRural = input("(U)rban or (R)ural setting: ")
age = 2020 - birthY
if(bankYearsAmount > 10 and child >= 2):
  print("APROBADO")
elif(civilS == "C" and child > 3 and (age >= 45 and age <= 55)):
  print("APROBADO")
elif(I >= 2500000 and civilS == "S" and urbRural == "U"):
  print("APROBADO")
elif(I >= 3500000 and bankYearsAmount > 5):
  print("APROBADO")
elif(urbRural == "R" and civilS == "C" and child < 2):
  print("APROBADO")
else:
  print("RECHAZADO")