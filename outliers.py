'''
numLst=[]
n = 9119
s = str(n)
for i in s:
    numLst.append((int(i)**2))

s = map(str, numLst)
s = ''.join(s)
s = int(s)
print(s)
'''
def square_digits(num):
    numLst=[]
    s = str(num)
    for i in s:
        numLst.append(int(i))

    newLst = sorted(numLst, key=int, reverse=True)
    s= map(str, newLst)
    s = ''.join(s)
    s = int(s)
    return s

#def Descending_Order(num):
#    return int("".join(sorted(str(num), reverse=True)))

mynum = square_digits(9119)
print(mynum)
