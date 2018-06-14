mySen = "g3ood 4of the2 pe6ople th5e Fo1r"
other = []

newSen = mySen.split()
for i in range(len(newSen)):
    other.append('')

for word in newSen:
    for i in word:
        try:
            if int(i):
                x = int(i) - 1
                other[x]= word
                print(other)
        except ValueError:
            pass

lsts = " ".join(other)
print(lsts)
