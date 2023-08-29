#Factores Primos
numero=int(input("Numero: "))
n_primos=[]
for i in range(2, numero + 1):
       while numero%i==0:
              numero=numero/i
              n_primos.append(i)
for i in n_primos:
       print(i)