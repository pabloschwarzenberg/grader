#para 1230
numero= int(input("ingrese su valor"))
unidad= numero%10
decena=(numero%100)//10
centena=(numero%1000)//100
unidadDeMil=numero//1000
print(unidadDeMil,"M+",centena,"C+",decena, "D+",unidad, "U")     