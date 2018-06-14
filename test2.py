import string
import random

def getUserString():
    usr_str = input('Enter your phrase: ')
    return usr_str

def generateRandomPhrase():
    str_usr_entered = getUserString()
    space_indices = [i for i, x in enumerate(str_usr_entered) if x == " "]
    str_usr_entered_no_spaces = str_usr_entered.replace(" ","")
    len_str_usr_entered_no_spaces = len(str_usr_entered_no_spaces)
    rand_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(len_str_usr_entered_no_spaces))
    ran_and_indicies = []
    ran_and_indicies.append(space_indices)
    ran_and_indicies.append(rand_str)
    ran_and_indicies.append(str_usr_entered_no_spaces)
    return ran_and_indicies

def scorePhrase():
    score = 0
    counter = 0
    list_w_indicies_and_ran_phrase = generateRandomPhrase()
    indicies_list = list_w_indicies_and_ran_phrase[0]
    rand_str_list = list_w_indicies_and_ran_phrase[1]
    str_usr_entered_no_spaces = list_w_indicies_and_ran_phrase[2]

    for i in range(len(str_usr_entered_no_spaces)):
        if rand_str_list[i] == str_usr_entered_no_spaces[i]:
            score +=1
    return score


strr = scorePhrase()
print(strr)
