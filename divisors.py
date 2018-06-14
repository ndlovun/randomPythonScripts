num = 13
rtrn=[]
for i in range(2, num):
    if num%i == 0:
        rtrn.append(i)

if rtrn == []:
    print(str(num) + " is prime!")
else:
    print(rtrn)


#same as above but more concise
def divisors(num):
    l = [a for a in range(2,num) if num%a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l
