def numero_perfecto(a):
    divi = 0

    for i in range(1, a):
        if a % i == 0:
            divi += i

    return divi == a
    
if __name__=="__main__":
    a=int(input("Ingrese a: "))
    perfecto=numero_perfecto(a)
    print(numero_perfecto(a))
    if perfecto:
      print("True")
    else:
      print("False")