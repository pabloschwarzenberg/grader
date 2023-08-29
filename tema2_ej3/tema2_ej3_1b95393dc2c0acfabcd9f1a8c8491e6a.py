def numero_perfecto(a):
    suma= 0 #recipiente.
    for suma_divisores in range(1,a):
        if a%suma_divisores== 0: #si el resto es cero, significa que es una división exacta.
            suma+= suma_divisores
    if suma==a:
      return True
    else:
      return False

if __name__=="__main__":
    a=int(input("Ingrese a: "))
    print("La suma de sus divisores es: " ,(numero_perfecto(a)))