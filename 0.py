def enumeration(x) :
    result = []
    for i in range(len(x)):
        result.append((i+1,x[i]))
    return result