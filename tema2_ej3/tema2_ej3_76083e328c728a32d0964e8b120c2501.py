def numero_perfecto(a):
    div_a = [i for i in range(1,a) if a % i==0]
    sumadiv_a = 0
    for j in div_a:
        sumadiv_a = j + sumadiv_a
    if sumadiv_a == a:
        return True
    else:
        return False

if __name__ == "__main__":
    a = int(input("ingrese numero"))
    print(numero_perfecto(a))        









    
           