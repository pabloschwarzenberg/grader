#Contestador de celular
NT = int(input("ingrese numero telefonico de 8 cifras:"))
H = int(input("ingrese hora de su llamada entre 0 y 23:"))

j = NT[4]
i = NT[5]
k = NT[6]
a = "9"
b = "0"
c = "9"
l = NT[0]
n = NT[1]
m = NT[2]
d = "8"
e = "7"

if H >= 0 and H <= 7:
   print("NUmero telefonico:", NT)
   print("Horario de su llamada:", H)
   print("Resultado: Contestar")
elif H > 7 and H <= 14:
   if(j==a and i==b and k==C):
     print("NUmero telefonico:", NT)
     print("Horario de su llamada:", H)
     print("Resultado: Contestar")
   else:
     print("Numero telefonico:", NT)
     print("Horario de su llamada:", H)
     print("Resultado: No contestar")
elif(H >= 17 and H <= 19):
   if(l==d and n==e and m==n):
     print("NUmero telefonico:", NT)
     print("Horario de su llamada:", H)
     print("Resultado: No contestar")
   else:
     print("Numero telefonico:", NT)
     print("Horario de su llamada:", H)
     print("Resultado: Contestar:")
else:
  print("Numero telefonico:", NT)
  print("Horario de su llamad:", H)
  print("Resultado: No contestar")
