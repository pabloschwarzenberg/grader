def validar_expresion(exp):
    def cosa(exp,i):
        try:
            if exp[i] in ["-","+"]:
                try:
                    if exp[i+1] in ["-","+"]:
                        print(exp[i+1])
                        return False
                    else:
                        print("!")
                        return cosa(exp,i+1)
                except:
                    print(exp[i])
                    return False
            elif exp[i] in ["1","2","3","4","5","6","7","8","9","0"]:
                try:
                    if exp[i+1] in ["-","+"]:
                        try:
                            if exp[i+2] in ["-","+"]:
                                print(exp[i+2])
                                return False
                            else:
                                return cosa(exp,i+1)
                        except:
                            return False
                    else:
                        print("!")
                        return cosa(exp,i+1)
                except:
                    print(exp[i])
                    return True
            else:
                print("!")
                return cosa(exp,i+1)
        except:
            return True
    return cosa(exp,0)

if __name__=="__main__":
    print(validar_expresion("2+3"))
    print(validar_expresion("2-3"))
    print(validar_expresion("2++"))
    print(validar_expresion("--2"))
    print(validar_expresion("2-"))