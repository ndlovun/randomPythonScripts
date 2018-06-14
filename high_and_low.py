import re

numbers = "23 2 3 4 8 99 5 2 5"
numRegex = re.compile(r'\s')
newNum = numRegex.sub(',',numbers)

newNum2 = [int(s) for s in newNum.split(',')]

numLst=[]
for i in (newNum2):
    numLst.append(i)

hv = str(max(numLst))
lv = str(min(numLst))
ans = hv + " " + lv
#print(max(numLst), " ",min(numLst))
print(ans)
