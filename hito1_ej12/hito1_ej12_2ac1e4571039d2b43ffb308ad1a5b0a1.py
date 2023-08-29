#Juego adivina mi número                                                                                         
from time import sleep
from random import randint
                                                                      
while True:                                                           
    numero = int(input("Ingrese un numero"))                          
    secret = randint(1,20)                                            
    if numero == secret:                                              
        sleep(1)                                                      
        print("Adivinaste, mi número era ", secret)                   
                                                                      
    if numero != secret:                                              
        if numero > secret:                                           
            print("mi número es menor")                               
        if numero < secret:                                           
            print("mi número es mayor")                               
        print("Intento N°2")                                          
        sleep(1)                                                      
        numero = int(input("Ingrese un numero"))                      
        if numero != secret:                                          
            if numero > secret:                                       
                print("mi número es menor")                           
            if numero < secret:                                       
                print("mi número es mayor")                           
            print("Intento N°3")                                      
            sleep(1)                                                  
            numero = int(input("Ingrese un numero"))                  
            if numero != secret:                                      
                if numero > secret:                                   
                    print("mi número es menor")                       
                if numero < secret:                                   
                    print("mi número es mayor")                       
                print("Intento N°4")                                  
                sleep(1)                                              
                numero = int(input("Ingrese un numero"))              
                if numero != secret:                                  
                    if numero > secret:                               
                        print("mi número es menor")                   
                    if numero < secret:                               
                        print("mi número es mayor")                   
                    print("Intento N°5")                              
                    print("No adivinaste, mi número era ",secret)     
                    sleep(1)                                          
                    break