#Descomponer un número
n = input("numero: ")

if len(n) == 4:
    print(eval(n[0]),"M+",eval(n[1]),"C+",eval(n[2]),"D+",eval(n[3]),"U")
if len(n) == 3:
    print(eval(n[0]),"C+",eval(n[1]),"D+",eval(n[2]),"U")
if len(n) == 2:
    print(eval(n[1]),"D+",eval(n[2]),"U")
if len (n) ==1:
    print(eval(n),"U")
