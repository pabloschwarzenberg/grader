def interpretar(expresion):
    operators = list()
    first = ["*", "/"]
    second = ["+", "-"]
    for i in expresion:
        if i in first or i in second:
            operators.append(i)
    nums = expresion.replace("*", " ").replace("/", " ").replace("+", " ").replace("-", " ").split()
    
    
    
    for i in range(len(operators)):
        if operators[i] in first:
            oper = nums[i]+operators[i]+nums[i+1]
            return interpretar(expresion[:expresion.find(oper)]+str(eval(oper)) + expresion[expresion.find(oper[-1])+1:])
    for i in range(len(operators)):
        if operators[i] in second:
            oper = nums[i]+operators[i]+nums[i+1]
            return interpretar(expresion[:expresion.find(oper)]+str(eval(oper)) + expresion[expresion.find(oper[-1])+1:])
    return expresion[:8]
    
        
    
    
    
        
    
        
    
    
                 

resultado=interpretar("2*3+5+6*7/9")
print(resultado)
#el resultado debiera ser 15.66666
