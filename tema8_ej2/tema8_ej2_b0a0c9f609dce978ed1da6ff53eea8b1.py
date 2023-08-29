def buscarTodas(palara,letra):
    arr_res = []
    if letra in palara:
        for index in range(0,len(palara)):
            if palara[index] == letra:
                arr_res.append(str(index))
        return " ".join(arr_res)

if __name__ == "__main__":
    pass
           