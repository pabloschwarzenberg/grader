def numero_perfecto(a):
      contador=1
      divisoresa=[]
      sumadivisoresa=0
      while contador<a:
        if a%contador==0:
          divisoresa.append(contador)
        contador+=1
      suma=0
      for i in divisoresa:
          suma=suma+i
      if suma==a:
        return True
      else:
        return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           