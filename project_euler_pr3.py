#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

primes_lst =[]

for i in range(1, 11):
    for x in range(2, 11):
        if i % x == 0:
            pass
        elif 1%x:
            primes_lst.append(i)

print(primes_lst)
