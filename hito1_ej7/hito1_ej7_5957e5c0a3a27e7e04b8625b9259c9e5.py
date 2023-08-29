A =int(input("ingrese dia de nacimiento: "))
B =int(input("ingrese Mes de nacimiento: "))
C =["Capricornio", "Acuario", "Piscis", "Aries", "Tauro", "Gemenis", "Cáncer", "león", "Virgo", "Libra",
    "Escorpión", "Sagitario","Capricornio"]
D =[20,19,21,20,21,21,23,22,23,23,22,22]

B =B-1
if A>D[B]:
    B = B+1

elif (B==12):
     B =1

print(C[B])    