#Contestador de celular
print("su telefono suena... rin..rin")
numero = int(input("ingrese el numero que me llama: "))
hora = int(input("ingrese que hora es: "))
if (hora>=0 and hora<=7) or (hora>=17 and hora<=19 and numero!=87765545) or (numero==77389909 and hora<=14):
    print("CONTESTAR")
else:
 print("NO CONTESTAR")