def high_and_low(numbers):
    newNum2 = [int(s) for s in numbers.split()]
    evnLst=[]
    oddLst=[]
    for i in (newNum2):
        if i%2 == 0:
            evnLst.append(newNum2.index(i))
        else:
            oddLst.append(newNum2.index(i))

    if len(evnLst) > len(oddLst):
        return oddLst[0] + 1
    else:
        return evnLst[0] + 1

    return ans

myNum = high_and_low("1 2 2")
print(myNum)
