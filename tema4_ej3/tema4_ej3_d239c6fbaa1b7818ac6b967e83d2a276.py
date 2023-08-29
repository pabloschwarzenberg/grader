a='perro'
def jerigonzo(texto):
    pres=[]
    mov=0
    vocal='aeiou'
    while mov<len(texto):
        print(mov)
        pres.append(texto[mov])
        if texto[mov] in vocal:
            if texto[mov]=='a':
                pres.append('pa')
            elif texto[mov]=='e':
                print('pas')
                pres.append('pe')
            elif texto[mov]=='i':
                pres.append('pi')   
            elif texto[mov]=='o':
                pres.append('po')            
            elif texto[mov]=='u':
                pres.append('pu')
        mov=+1
    return print(*pres)
            