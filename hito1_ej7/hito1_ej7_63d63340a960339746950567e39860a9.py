#Zodiaco
dia=int(input("escriba el dia de nacimiento: "))
mes=int(input("escriba su mes de nacimiento: "))
if mes==1 and 20<=dia or mes==2 and 18>=dia:
    print("es acuario")
elif mes==2 and 19<=dia or mes==3 and 20>=dia:
    print("es piscis")
elif mes==3 and 21<=dia or mes==4 and 19>=dia:
    print("es aries")
elif mes==4 and 20<=dia or mes==5 and 20>=dia:
    print("es tauro")
elif mes==5 and 21<=dia or mes==6 and 20>=dia:
    print("es geminis")
elif mes==6 and 21<=dia or mes==7 and 22>=dia:
    print("es cancer")
elif mes==7 and 23<=dia or mes==8 and 22>=dia:
    print("es leo")
elif mes==8 and 23<=dia or mes==9 and 22>=dia:
    print("es virgo")
elif mes==9 and 23<=dia or mes==10 and 22>=dia:
    print("es libra")
elif mes==10 and 23<=dia or mes==11 and 21>=dia:
    print("es escorpión")
elif mes==11 and 22<=dia or mes==12 and 21>=dia:
    print("es sagitario")
else:
    print("es capricornio")
