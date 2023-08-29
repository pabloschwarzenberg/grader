#Sistema de Ecuaciones
ingresar_a= float(input("Ingrese Numero para a: "))
ingresar_b= float(input("Ingrese Numero para b: "))
ingresar_c= float(input("Ingrese Numero para c: "))
ingresar_d= float(input("Ingrese Numero para d: "))
ingresar_e= float(input("Ingrese Numero para e: "))
ingresar_f= float(input("Ingrese Numero para f: "))
#INCOGNITAS
x=(ingresar_c * ingresar_e - ingresar_b * ingresar_f)//(ingresar_a * ingresar_e - ingresar_b * ingresar_d)
y=(ingresar_a * ingresar_f - ingresar_c * ingresar_d)//(ingresar_a * ingresar_e - ingresar_b * ingresar_d)
#SALIDAS
print("x="+str(x)+"y="+str(y))