import string
import random

#Gets string to be compared from user.
usr_str = input("Enter string to be compared: ")
space_indices = [i for i, x in enumerate(usr_str) if x == " "]
print('Original string: ' + usr_str)
print('Space indicies: ' + str(space_indices))

#Removes space from user string and computes string length with no spaces.
no_space_str = usr_str.replace(" ","")
usr_str_len = len(no_space_str)
print('Original string length: ' + str(usr_str_len))

#Generates random string that is the same length as user string with no spaces.
random_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(usr_str_len))
print('Random string: ' + random_str)
print('Random string length: ' + str(len(random_str)))

#Turns the random string into a list and then adds spaces to the random list at the same indicies that
#the user string has spaces then prints the random string with spaces.
usr_list = []
for i in random_str:
    usr_list.append(i)

for i in space_indices:
    usr_list.insert(i, " ")

print('Random string with spaces: '+''.join(usr_list))
