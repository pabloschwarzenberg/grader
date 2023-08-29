import random

def ocultar_letras(palabra,cantidad):
    n = cantidad
    
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1
    palabra_to_list = Convert(palabra)
    
    while n > 0:
        x = random.randint(0, len(palabra)-1)
        
        if palabra_to_list[x] != "_":
            palabra_to_list[x] = "_"
            n = n - 1
    
    return ''.join(palabra_to_list) 

def revisar_letra(palabra_secreta,palabra,letra):
    def Convert(string):
        list1=[]
        list1[:0]=string
        return list1
        
    list1 = Convert(palabra_secreta)
    list2 = Convert(palabra)
    
    for i in range(0,len(palabra_secreta)):
        if list2[i] == "_":
            if list1[i] == letra:
                list2[i] = letra
    
    
    return ''.join(list2)

if __name__ == "__main__":
    pass
         