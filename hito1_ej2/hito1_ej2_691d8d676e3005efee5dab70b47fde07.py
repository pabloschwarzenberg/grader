#Contestador de celular
num=int(input("ingrese su número: "))
hora=int(input("ingrese su hora: "))
num=str(num)
if hora>=0 and hora<=7:
    print("contestar")
elif hora<14 and num[5:8]=="909":
    print("contestar")
elif hora>=17 and hora<=19 and num[0:3]!="877":
    print("contestar")
else:
    print("no contestar")