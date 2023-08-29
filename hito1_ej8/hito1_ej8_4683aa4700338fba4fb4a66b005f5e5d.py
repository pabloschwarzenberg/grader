#Descomponer un número
def descomponer(num_str):
    if len(num_str) == 1:
        return num_str + 'U'
    
    elif len(num_str) == 2:
        return num_str[0] + 'D + ' + num_str[1] + 'U'
    
    elif len(num_str) == 3:
        return num_str[0] + 'C + ' + num_str[1] + 'D + ' + num_str[2] + 'U'
    
    else:
        return num_str[0] + 'M + ' + num_str[1] + 'C + ' + num_str[2] + 'D + ' + num_str[3] + 'U'
    
num = input()
print(descomponer(num))      