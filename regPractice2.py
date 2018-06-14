import re
testlst = ['Alice eats apples.','Bob pets cats.',
            'Carol throws baseballs.','Alice throws Apples.','BOB EATS CATS.',
             'Robocop eats apples.', 'ALICE THROWS FOOTBALLS.','Carol eats 7 cats.']

cnt=0
rsltlst=[]
didnomatch=[]
for i in range(len(testlst)):
    regx = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.',re.I)#'[eats pets throws][apples cats baseballs]')
    match = regx.search(testlst[cnt])
    if match:
        rsltlst.append(match.group())
    else:
        didnomatch.append(testlst[cnt])

    cnt+=1


print('These matched:', rsltlst)
print('These did not match:', didnomatch)
