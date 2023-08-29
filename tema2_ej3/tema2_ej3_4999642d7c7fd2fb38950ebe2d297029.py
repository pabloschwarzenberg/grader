def numeros_perfectos(n):
     divisores = []
     for i in range(1, n):
         if n%i == 0:
             i = divisores.append(i)
             
     ##Sumar divisores 
     suma = 0
     for divisor in divisores:
         suma = suma + divisor 
     if suma == n:
         esPerfecto = True
     else: 
         esPerfecto = False 
     return esPerfecto 
if __name__=="__main__":
    a=int(input("ingrese a: "))
    print(numero_perfecto(a))
