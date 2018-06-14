def multiples():
    numlst=[]
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            numlst.append(i)
    return sum(numlst)

num = multiples()
print(num)
