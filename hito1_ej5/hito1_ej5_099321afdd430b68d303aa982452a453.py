#Cálculo del dígito verificador de un rut
num = input("ingrese un numero: ")
def digitoUTFSM(num):
  s=str(num)[::-1]
  values = [2, 3, 4, 5, 6, 7]
  total=sum([int(s[i])*values[i%6] for i in range(len(s))])
  return 11-(total%11)

if digitoUTFSM(num) == 11:
  print("dv=0")
elif digitoUTFSM(num) == 10:
  print("dv=k")
else:
  print("dv=",digitoUTFSM(num))      