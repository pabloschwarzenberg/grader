#Cálculo del dígito verificador de un rut
rut=int(input())
unidad=rut%10
decena=(rut%100)//10
centena=(rut%1000)//100
unidadmil=(rut%10000)//1000
decenamil=(rut%100000)//10000
centenamil=(rut%1000000)//100000
unidadmi=(rut%10000000)//1000000
decenami=(rut%100000000)//10000000
operacion=unidad*2+decena*3+centena*4+unidadmil*5+decenamil*6+centenamil*7+unidadmi*2+decenami*3
operacion2=operacion%11
resultado=11-operacion2
if resultado==11:
    print("dv=", 0)
elif resultado==10:
    print("dv=", "k")
else:
    print("dv=", resultado)
     