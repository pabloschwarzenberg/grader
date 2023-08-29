verificar= False
numero=0
for i in range(1,numero+1):
    if (numero% i)==0:
       contador = contador + 1
    if contador >= 3:
        verificar=True
        break

if __name__ == "__main__":
  numero = int(input("inserta un numero: "))
  if contador==2 or verificar==False:
    print("True")
  else: 
    print ("False")
     