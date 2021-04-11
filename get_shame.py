from bs4 import BeautifulSoup


def listToString(s): 
    str1 = ""  
    for ele in s: 
        str1 += ele  
    return str1 

def preData(tr):
    predataArr = []
    index      = 0  
    if(tr == 1):
        for x in range(len(tempCheckP)):
            index1 = index1 + 1
            if (tempCheckP[x] == '-'):
                index1 = index1
                break
        preData2(1)
    else:
        for x in range(len(tempCheckSc)):
            index2 = index2 + 1
            if (tempCheckSc[x] == '-'):
                index2 = index2
                break
        preData2(2)




def preData2(tr):
    pred = []
    if(tr == 1):
        for z in range(index1, len(tempCheckP)):
            tempCheckP2.append(tempCheckP[z])
            pred = tempCheckP2

    else:
        for n in range(index2, len(tempCheckSc)):
            tempCheckSc2.append(tempCheckSc[n])
            pred = tempCheckSc2
        
    data = str(listToString(pred)) 
    
    return result.append(data)
    
    

attrs        = []
tr_gb        = []

tempCheckSc  = ''
tempCheckSc2 = []

tempCheckP   = '' 
tempCheckP2  = []

index1       = 0
index2       = 0
result       = []


html_doc = """

<i piintu-root = "1"> Data </i>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

listTag = [tag.name for tag in soup.find_all()]


for elm in soup():
    attrs = attrs + list(elm.attrs)

for i in range(len(attrs)):
    tempCheck = str(attrs[i])
    #print(tempCheck)
    if ("piintu-" in tempCheck ):
        tempCheckP  = list(tempCheck)
        tr_gb.append(1)
    elif ("sc-" in tempCheck ):
        tempCheckSc = list(tempCheck)
        tr_gb.append(2)


if tempCheckP != '':
    for x in range(len(tempCheckP)):
        index1 = index1 + 1
        if (tempCheckP[x] == '-'):
            index1 = index1
            break

    for z in range(index1, len(tempCheckP)):
        tempCheckP2.append(tempCheckP[z])

    data = str(listToString(tempCheckP2)) 
    result.append(data)


if (tempCheckSc != ''):
    for x in range(len(tempCheckSc)):
        index2 = index2 + 1
        if (tempCheckSc[x] == '-'):
            index2 = index2
            break

    for n in range(index2, len(tempCheckSc)):
        tempCheckSc2.append(tempCheckSc[n])

    data2 = str(listToString(tempCheckSc2)) 
    result.append(data2)



print(result)

