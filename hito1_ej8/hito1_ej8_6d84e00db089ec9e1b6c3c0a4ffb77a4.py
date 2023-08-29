numero=int(input("Ingrese un número de cuatro dígitos: "))
#unidad
unidad=(numero%10)
print("La unidad es:",unidad,"U")
#decena
decena=int(((numero%100)-unidad)/10)
print("La decena es:",decena,"D")
#centena
centena=int(((numero%1000)-(numero%100))/100)
print("La centena es:",centena,"C")
#miles
miles=int(((numero%10000)-(numero%1000))/1000)
print("Los miles son:",miles,"M")
print("La descomposición es:",miles,"M","+",centena,"C","+",decena,"D","+",unidad,"U") 