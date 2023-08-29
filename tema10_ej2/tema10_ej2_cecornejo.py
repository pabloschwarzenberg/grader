#La función debe retornar la distancia como un string
# +1 : si la distancia es mayor que 1
# IB : si la distancia es 1, y para llegar de una palabra a la otra hay que
#      insertar o borrar una letra
# 1S : si la distancia es 1 porque hay que sustituir una letra
# 0D : si las palabras son iguales
palabra1= input("ingrese la primera palabra: ")
palabra2= input("ingrese la segunda palabra: ")

def levenshtein(palabra1,palabra2):
  palabra1= input("ingrese la primera palabra: ")
palabra2= input("ingrese la segunda palabra: ")


if palabra1 == palabra2 :
    print("la distancia es 0")


elif len(palabra1)==len(palabra2):
    error=0
    for i in range(len(palabra1)):
        x=palabra1[i]
        y=palabra2[i]
        if x!=y:
            error+=1

    if error==1:
        print("1 operación (sustituir)")
    elif error>1:
        print("más de una operacion, chupalo")

elif len(palabra1)!= len(palabra2):
    #CODIGO DICE QUE SI HAY MÁS DE DOS LETRAS DE DIFERENCIAS
    if (len(palabra1)-len(palabra2))>=2 or (len(palabra2)-len(palabra1))>=2 :
        print("más de una operación")
        
    #EL SIGUIENTE CÓDIGO SOLO VE SI FALTA UNA LETRA AL INICIO O AL FINAL
    elif (len(palabra1))-(len(palabra2))==1 or (len(palabra2))-(len(palabra1))==1 :

        if len(palabra1)> len(palabra2):
            larga= list(palabra1)
            corta= list(palabra2)

        elif len(palabra2)>len(palabra1):
            larga=list(palabra2)
            corta=list(palabra1)

        error=0
        for i in range(len(corta)):
            x= larga[i]
            y= corta[i]
            if x!=y:
                error+=1

        if error==0:
            print("1 operación, sobra/falta una letra al final")

        #PUEDE FALTAR UNA LETRA AL MEDIO O AL INICIO
        elif error>=1:
            larga.pop(0)
            if larga==corta:
                print("1 operación, poner/quitar letra al inicio")

            else:
                
                if len(palabra1)> len(palabra2):
                    larga2= list(palabra1)
                    corta2= list(palabra2)

                elif len(palabra2)>len(palabra1):
                    larga2=list(palabra2)
                    corta2=list(palabra1)
                        
                error2=0
                for i in range(len(corta2)):
                    e= larga2[i]
                    f= corta2[i]
                    if e!=f:
                        error2 +=1
                        larga2.pop(i)     #OJO AQUÍ!! CON "POP" SE ALTERA LA LISTA ORIGINAL!!!   

                if error2 == 1:
                    
                    if larga2==corta2:
                        print("1 operación insertar/quitar letra al medio")

                else:
                    print("más de una operacion, chupalo")
   
    pass

if __name__=="__main__":
    pass
           