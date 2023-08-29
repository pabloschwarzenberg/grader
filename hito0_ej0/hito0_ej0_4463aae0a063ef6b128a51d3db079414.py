import math

def suma(string):
    string=string.split('+')
    for i in range(2):
        if '_' in string[i]:
            string[i]='-'+string[i][1:]
    suma=float(string[0])+float(string[1])
    return str(suma)

def resta(string):
    string=string.split('-')
    for i in range(2):
        if '_' in string[i]:
            string[i]='-'+string[i][1:]
    resta=float(string[0])-float(string[1])
    return str(resta)

def producto(string):
    string=string.split('*')
    for i in range(2):
        if '_' in string[i]:
            string[i]='-'+string[i][1:]
    producto=float(string[0])*float(string[1])
    return str(producto)

def cuociente(string):
    string=string.split('/')
    for i in range(2):
        if '_' in string[i]:
            string[i]='-'+string[i][1:]
    cuociente=float(string[0])/float(string[1])
    return str(cuociente)

def modify(string):
    #Función para manejar los números negativos
    while '--' in string:
        this_pos=string.find('--')
        string=list(string)
        string[this_pos+1]='_'
        string=''.join(string)
    if string[0]=='-':
        string='_'+string[1:]
    return string

def nextno(string,pos):
    #Función que, dada la posición de un operador en el string, encuentra la posición del último dígito del número siguiente
    nos=['0','1','2','3','4','5','6','7','8','9','.','_']
    index=-1
    for thing in range(pos+1,len(string)):
        if string[thing] not in nos:
            index=thing
            break
    if index==-1:
        index=len(string)
    return index-1

def interpretar(string):
    string=modify(string)
    if '*' in string or '/' in string:
        mul_index=string.find('*')
        div_index=string.find('/')
        op_indexes=[mul_index,div_index]
        if -1 in op_indexes:
            op_indexes.remove(-1)
        first_operator=min(op_indexes)
        next_number=nextno(string,first_operator)
        string=list(string)
        string.reverse()
        string=''.join(string)
        last_number=len(string)-nextno(string,len(string)-first_operator-1)-1
        string=list(string)
        string.reverse()
        substring=''
        if string[first_operator]=='*':
            whatt='multiply'
        elif string[first_operator]=='/':
            whatt='divide'
        for to_del in range(last_number,next_number+1):
            substring+=string.pop(last_number)
        if whatt=='multiply':
            string.insert(last_number,modify(producto(substring)))
        else:
            string.insert(last_number,modify(cuociente(substring)))
        string=''.join(string)
        return interpretar(string)
    if '+' in string or '-' in string:
        plu_index=string.find('+')
        min_index=string.find('-')
        op_indexes=[plu_index,min_index]
        if -1 in op_indexes:
            op_indexes.remove(-1)
        first_operator=min(op_indexes)
        next_number=nextno(string,first_operator)
        string=list(string)
        string.reverse()
        string=''.join(string)
        last_number=len(string)-nextno(string,len(string)-first_operator-1)-1
        string=list(string)
        string.reverse()
        substring=''
        if string[first_operator]=='+':
            whatt='add'
        elif string[first_operator]=='-':
            whatt='substract'
        for to_del in range(last_number,next_number+1):
            substring+=string.pop(last_number)
        if whatt=='add':
            string.insert(last_number,modify(suma(substring)))
        else:
            string.insert(last_number,modify(resta(substring)))
        string=''.join(string)
        return interpretar(string)
    if string[0]=='_':
        string='-'+string[1:]
    return math.trunc(float(string)*10**5)/10**5

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666