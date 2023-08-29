#Contestador de celular
def menu():
 print("""Planes de telefono
1.- Plan A
2.- Plan B""")

menu()

planes=int(input("Ingrese el plan que corresponde: "))
print("")

tiempo=int(input("Ingrese el tiempo de la llamada: "))
print("")

resto=tiempo%5
if(tiempo<=5):
  valor=tiempo*10
elif(tiempo>5 and tiempo<9):
  valor=50+resto*8
elif(tiempo>8 and tiempo<11):
  valor=74+resto*7
else:
  valor=88+(tiempo-10)*5
  
if(planes==1):
    print("Costo de la llamada: ",valor*1.03)

elif(planes==2):
    print("Costo de la llamada: ",valor*1.05)
