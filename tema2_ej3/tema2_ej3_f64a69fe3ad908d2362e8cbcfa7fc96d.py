def numero_perfecto(a):
    div = []
    for x in range(1, a):
      if a%x == 0:
        div.append(x)
    y = sum(div)
    if y == a:
      return True
    else:
      return False
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print(numero_perfecto(a))
           