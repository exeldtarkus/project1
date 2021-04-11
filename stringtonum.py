import string

def splitData(splitStr):
    for i in range(len(splitStr)):
        if (splitStr[i].isnumeric() == True):
            number = int(splitStr[i])
            tempNum.append(number)

        if (splitStr[i].isnumeric() == False):
            tempOps.append(splitStr[i])

def evaluate (strParam):
    splitData(strParam)
    if (tempOps[0] == '+'):
        result = int(tempNum[0]) + int(tempNum[1])
    elif (tempOps[0] == '-'):
        result = int(tempNum[0]) - int(tempNum[1])
    NumCntIndx = 2
    #print('NumCntIndx',NumCntIndx)
    #print ('1Result :',result)
    
    for oprSelect in range(len(tempOps)-1):
        oprSelect  = oprSelect + 1
        #print('oprSelect',oprSelect)
        if (tempOps[oprSelect] == '+'):
            result = result + tempNum[NumCntIndx]
            #print(result ,'=',result,'+', tempNum[NumCntIndx])
            #break
        elif (tempOps[oprSelect] == '-'):
            result = result - tempNum[NumCntIndx]
            #print(result ,'=',result,'-', tempNum[NumCntIndx])
        NumCntIndx = NumCntIndx + 1
        #print('NumCntIndx-M',NumCntIndx)
    return result

number     = (1,2,3,4,5,6,7,8,9)
opratorJum = ('+','-')
tempNum    = []
tempOps    = []
result     = 0



while True:
    try:
        numStr = input('Input Data :')
        evaluate = evaluate(numStr)
        print(str(numStr), '=',evaluate)
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except UnboundLocalError:
        print('Value Inputan Error')
    







