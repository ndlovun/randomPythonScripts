import re

testlst = [' weak@pa@ss'] #Enter test string here.

cnt=0
rsltlst=[]
didnomatch=[]
for i in range(len(testlst)):
    regx = re.compile(r'[^0-9a-zA-Z\s]') #enter regex here.
    match = regx.search(testlst[cnt]) #enter method here search or findall etc....
    if match:
        rsltlst.append(match.group())
    else:
        didnomatch.append(testlst[cnt])

    cnt+=1


print('These matched:', rsltlst)
print('These did not match:', didnomatch)
