telefono = int(input("ingrese el numero que llama: "))
hora = int(input("ingrese la hora: "))
if hora < 7 or hora < 14 and str(telefono).endswith('909') or 17 <= hora < 19 and not str(telefono).startswith('877'):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")