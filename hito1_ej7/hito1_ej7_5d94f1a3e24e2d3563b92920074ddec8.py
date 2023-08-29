#Zodiaco
dia= int(input("ingrese dia:"))
mes= int(input("ingrese mes:"))

if mes==3 and 21<=dia or mes==4 and 20>=dia:
    print("Aries")
elif mes==4 and 21<=dia or mes==5 and 21>=dia:
    print("Tauro")
elif mes==5 and 22<=dia or mes==6 and 21>=dia:
    print("Geminis")
elif mes==6 and 22<=dia or mes==7 and 22>=dia:
    print("Cancer")
elif mes==7 and 23<=dia or mes==8 and 22>=dia:
    print("Leo")
elif mes==8 and 23<=dia or mes==9 and 23>=dia:
    print("Virgo")
elif mes==9 and 24<=dia or mes==10 and 23>=dia:
    print("Libra")
elif mes==10 and 24<=dia or mes==11 and 22>=dia:
    print("Escorpion")
elif mes==11 and 23<=dia or mes==12 and 21>=dia:
    print("Sagitario")
elif mes==12 and 22<=dia or mes==1 and 20>=dia:
    print("Capricornio")
elif mes==1 and 21<=dia or mes==2 and 19>=dia:
    print("Acuario")
elif mes==2 and 20<=dia or mes==3 and 20>=dia:
    print("Picis")
        