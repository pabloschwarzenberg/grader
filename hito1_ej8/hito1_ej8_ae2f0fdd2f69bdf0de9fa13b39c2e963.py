#Descomponer un número
codigo=eval(input("numero:"))
nVeces = codigo % 1000
aux = codigo // 1000 #este es 1
nVeces2 = nVeces % 100
aux2 = nVeces // 100
nVeces3 = nVeces2 % 10
aux3= nVeces2 // 10
print(aux)
print(aux2)
print(nVeces3)
print(aux3)
print(aux,"M","+",aux2,"C","+",aux3,"D","+",nVeces3,"U")      