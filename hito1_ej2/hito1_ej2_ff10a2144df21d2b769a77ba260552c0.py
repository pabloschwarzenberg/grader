#Contestador de celular
numero=int(input())
hora=int(input())
assert 0<=hora<=23

if 0<=hora<7:
    print("CONTESTAR")
    
if 7<=hora<14:
    if numero%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if 17<=hora<=19:
    if numero//100000==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
if 23>=hora>19:
    print("NO CONTESTAR")