N = int(input("ingrese un numero de 8 cifras telefonico: "))
H = int(input("ingrese hora de la llamada: "))

N = str(N)
N_2 = N[0:3]
print(N_2)
N_3 = N[5:9]
print(N_3)

if H >= 0 and H <= 7 :
    print("contestar")
elif H >= 7 and H <= 14:
    if N_3 == 909:
        print("no contestar")
    else:
        print("CONTESTAR")
elif H >= 17 and H <= 19 :
    if N_2 == N[0:3]:
        print("no contestar")
    else:
        print("contestar")
elif H > 19:
    print("no contestar")                    
      