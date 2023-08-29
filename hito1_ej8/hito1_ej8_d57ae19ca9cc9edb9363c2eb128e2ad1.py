#Descomponer un número
numero= str(input("ingrese un numero entero de hasta 4 digitos"))
numero2= str(numero)
if len(numero2)==4:
  a= str(numero2[0]+"M")
  b= str(numero2[1]+"C")
  c= str(numero2[2]+"D")
  d= str(numero2[3]+"U")
  print(a,"+",b,"+",c,"+",d)
elif len(numero2)==3:
  f= str(numero2[0]+"C")
  e= str(numero2[1]+"D")
  g= str(numero2[2]+"U")
  print(f,"+",e,"+",g)
elif len(numero2)==2:
  f= str(numero2[0]+"D")
  e= str(numero2[1]+"U")
  print(f,"+",e)
elif len(numero2)==1:
  e= str(numero2[0]+"U")
  print(e)