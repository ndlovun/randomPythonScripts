import re

testlst = [' weak@pa@ss']

cnt=0
rsltlst=[]
didnomatch=[]
for i in range(len(testlst)):
    regx = re.compile(r'[^0-9a-zA-Z\s]')
    match = regx.search(testlst[cnt])
    if match:
        rsltlst.append(match.group())
    else:
        didnomatch.append(testlst[cnt])

    cnt+=1


print('These matched:', rsltlst)
print('These did not match:', didnomatch)
