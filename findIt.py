'''
tsLst = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
dicti = {i:tsLst.count(i) for i in tsLst}
for i in dicti.values():
    if i%2:
        spNum=i

d2 = dict(map(reversed, dicti.items()))
print(d2[spNum])
'''
def find_it(seq):
    dicti = {i:seq.count(i) for i in seq}
    for i in dicti.values():
        if i%2:
            spNum=i

    d2 = dict(map(reversed, dicti.items()))
    return d2[spNum]

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))
