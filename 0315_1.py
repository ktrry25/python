X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T=70
result=[]
for i in X:
    for j in Y:
        for k in Z:
            result.append(i+j+k)
result_1=[]
result=list(set(result))
for i in result:
    if i == T:
        result_1.append(True)
    else:
        result_1.append(False)
    
result_1=tuple((result_1))
print(result)
print(result_1)