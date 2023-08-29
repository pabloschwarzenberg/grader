#Nota final
nombre=input("ingrese su nombre: ")
apellido=input("ingrese su apellido: ")

pt=float(input("ingrese su primera nota: "))
while(pt>7 or pt<1):
  pt=float(input("ingrese su primera nota: "))
  
pi=float(input("ingrese su segunda nota: "))
while(pi>7 or pi<1):
  pi=float(input("ingrese su segunda nota: "))

ne=float(input("ingrese su tercera nota: "))
while(ne>7 or ne<1):
  ne=float(input("ingrese su tercera nota: "))

pp=float(input("ingrese su cuarta nota: "))
while(pp>7 or pp<1):
  pp=float(input("ingrese su cuarta nota: "))


promedio=((0.3*pt) + (0.3*pi) + (0.3*ne) + (0.1*pp))
print(nombre,apellido,"tu promedio es",promedio)

if promedio>=4:
  print("Aprobaste")
else:
  print("Reprobaste, que mal")
      