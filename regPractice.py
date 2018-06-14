import re
'''
regx = re.compile(r'^[A-Z]\w*\s\bNakamoto\b')
match = regx.search('Satoshi nakamoto')
if match:
    print ('Match found: ', match.group())
else:
    print ('No match found!')
'''
testlst = ['Satoshi Nakamoto','Alice Nakamoto',
            'Robocop Nakamoto','satoshi Nakamoto',
            'Mr. Nakamoto', 'Nakamoto', 'Satoshi nakamoto']

cnt=0
rsltlst=[]
didnomatch=[]
for i in range(len(testlst)):
    regx = re.compile(r'[A-Z][a-z]*\sNakamoto')
    match = regx.search(testlst[cnt])
    if match:
        rsltlst.append(match.group())
    else:
        didnomatch.append(testlst[cnt])

    cnt+=1


print('These matched:', rsltlst)
print('These did not match:', didnomatch)
