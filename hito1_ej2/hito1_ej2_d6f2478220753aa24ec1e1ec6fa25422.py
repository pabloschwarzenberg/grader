N = int(input("ingrese un numero de telefono de 8 digitos"))
H = int(input("ingrese hora de llamada entre 0 y 23 horas"))
telefono = N
numero1 = N//10000000
numero2 = (N-(numero1*10000000))//1000000
numero3 = (N-(numero1*10000000)-(numero2*1000000))//100000
numero4 = (N-(numero1*10000000)-(numero2*1000000)-(numero3*100000))//10000
numero5 = (N-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000))//1000
numero6 = (N-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000)-(numero5*1000))//100
numero7 = (N-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000)-(numero5*1000)-(numero6*100))//10
numero8 = (N-(numero1*10000000)-(numero2*1000000)-(numero3*100000)-(numero4*10000)-(numero5*1000)-(numero6*100)-(numero7*10))
if 0 < H < 7:
    print("CONTESTAR")
elif numero6 == 9 and numero7 == 0 and numero8 == 9:
    print("CONTESTAR")
elif H < 14:
    print("NO CONTESTAR")
elif numero1 == 8 and numero2 == 7 and numero3 == 7:
    print("NO CONTESTAR")
elif 17 < H < 19:
    print("CONTESTAR")
elif H > 19:
    print("NO CONTESTAR")
