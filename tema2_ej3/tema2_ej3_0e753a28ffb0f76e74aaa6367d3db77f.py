def numero_perfecto(a):
  enteros=0
  perfecto=""
  for i in range(1,a):
    if a % i == 0:
      enteros= enteros + i
    if enteros == a:
      perfecto= True
    if enteros != a:
       perfecto= False
  return perfecto

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           