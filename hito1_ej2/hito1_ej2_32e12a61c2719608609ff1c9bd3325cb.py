#Contestador de celular
numero=int(input())
hora=int(input())
primeros=numero//100000
ultimos=numero-(numero//1000)*1000
if 0<=hora<=7 or (hora<=14 and ultimos==909) or ( 17<=hora<=19 and primeros!=877):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")