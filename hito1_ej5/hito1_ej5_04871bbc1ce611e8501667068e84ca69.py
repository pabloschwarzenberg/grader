#codigo verificador de rut
rut=int(input("ingrese su rut sin puntos ni guion ni codigo verificador:"))
one=((rut//1)%10)*2
two=((rut//10)%10)*3
three=((rut//100)%10)*4
four=((rut//1000)%10)*5
five=((rut//10000)%10)*6
six=((rut//100000)%10)*7
seven=((rut//1000000)%10)*2
eight=(rut//10000000)*3
suma=(one + two + three + four + five + six + seven + eight)
resto= suma%11
digv= 11-resto
if digv==11:
       print("dv= 0")
elif digv==10:
       print("dv=K")
else:
       print("dv= ",digv)
