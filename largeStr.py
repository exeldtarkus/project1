def largest(data):
    for i in range(len(data)):
        strArray.append(str(data[i]))
    return strArray


numArray = [1,10,100]
strArray = []

lisStr = largest(numArray)

str1 = ''.join(lisStr)

print(numArray, 'to', str1) 