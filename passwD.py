import re

def passChecker():
    pswd = input('A strong password is defined as one that is at least eight characters long,\n contains both uppercase and lowercase characters, and has at least one digit.\
                 \n Please enter new password: ')
    while len(pswd) < 8:
        print('Password is too short enter longer password!')
        pswd = input('Please enter new password: ')

    uppercaseCounter = 0
    digitCounter = 0
    indxCounter = 0

    
    for i in range(len(pswd)):
        regxL = re.compile(r'[A-Z]')
        matchL = regxL.search(pswd[indxCounter])
        regxD = re.compile(r'\d')
        matchD = regxD.search(pswd[indxCounter])

        if matchL:
            uppercaseCounter +=1
        elif matchD:
            digitCounter +=1


    if uppercaseCounter == 0 and digitCounter == 0:
        print('Password does not meet the requirements!')






passChecker()
