#Conversión de Decimal a Binario
print("hola bienvenido/a a la Conversión de Decimal a Binario")
a= float(input("ingrese un numero decimal"))
listado= []

while a>0 :
  b= int(a%2)
  listado.append(b)
  a=(a-b)/2
c=""
for d in listado [: :-1]:
  c= c + str(d)
  print("resultado=" +str (c))