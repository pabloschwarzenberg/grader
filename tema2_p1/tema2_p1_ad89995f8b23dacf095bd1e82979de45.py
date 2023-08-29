##3_numeros primos:
#Escriba una función llamada es_primo que retorne True cuando
#es un numero primo y False cuando no lo es
a=int(input("ingresar numero:"))

def es_primo (num):
    contador=0
    for i in range(1,num+1):
        if num % i ==0:
            contador+=1
            print(i)

    if contador==2:
        return True
    else:
        return False
    
print(es_primo(a))
           