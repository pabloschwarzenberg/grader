#Cálculo del dígito verificador de un rut
rut = int(input("Ingrese un rut porfavor: "))
print("descomponer rut")
print("descomponiendo el rut", rut/1000000)
print("descomponiendo el rut", rut/100000)
print("descomponiendo el rut", rut/10000)
print("descomponiendo el rut", rut/1000)
print("descomponiendo el rut", rut/100)
print("descomponiendo el rut", rut/10)
print("descomponiendo el rut", rut/1)

n1=(rut//10000000) * 3
print("resultado de n1: ",n1)
n2=((rut//1000000)%10) * 2
print("resultado de n2: ",n2)
n3=((rut//100000)%10) * 7
print("resultado de n3: ",n3)
n4=((rut//10000)%10) * 6
print("resultado de n4: ",n4)
n5=((rut//1000)%10) * 5
print("resultado de n5: ",n5)
n6=((rut//100)%10) * 4
print("resultado de n6: ",n6)
n7=((rut//10)%10) * 3
print("resultado de n7: ",n7)
n8=((rut//1)%10) * 2
print("resultado de n8: ",n8)
suma=(n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8)
print("El resultado de la suma es el siguiente: ",suma)
resto1= suma // 11
print("El resultado del primer resto es =suma // 11: ",resto1)
resto2 = suma-(11*resto1)
print("El resultado del segundo resto es resto2=suma-(11*resto1): ",resto2)
resta=11-resto2
print("El resultado de la resta es=11-resto2: ",resta)
if resta == 11:
  print("dv=",end="")
  print(0)
elif resta == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print(resta)