#Descomponer un número
lista= []
def Descomponer(n):
  if int(num) <= 9999 :
    for i in num:
      lista.append(int(i))
  else:
    print("el numero contiene más de 4 digitos")
    
num = input("Introdusca el numero que quiera descomponer, que posea solo 4 digitos: ")
Descomponer(num)
nm = int(num)
if nm <= 9999 and nm >= 1000 :
    M = lista[0]
    C = lista[1]
    D = lista[2]
    U = lista[-1]

    print(M,"M + ",C, "C + ",D,"D + ",U," U ")

elif nm <= 999 and nm >= 100:
    C = lista[0]
    D = lista[1]
    U = lista[2]
    print(C, "C + ",D,"D + ",U," U ")
elif nm <= 99 and nm >= 10 :
    D = lista[0]
    U = lista[1]
    print(D,"D + ",U," U ")
else:
    U = lista[0]
    print(U,"U")
