def buscarTodas(a,b):
    string = ""
    for i in range(0,len(a)):
        if i == 0:
            if a[i] == b:
                string = str(i)
        elif a[i] == b:
            string = string+" "+str(i)
    return string
    pass

if __name__ == "__main__":
    pass
           