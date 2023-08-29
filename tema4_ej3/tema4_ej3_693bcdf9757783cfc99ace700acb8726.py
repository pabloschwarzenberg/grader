def jerigonzo(palabra):
    P_Jeringoso=''
    for letra in palabra:
        if letra in "AEIOUaeiou":
            P_Jeringoso += letra
            P_Jeringoso += 'p'
        P_Jeringoso += letra
    return P_Jeringoso


print(jerigonzo('Hola'))
