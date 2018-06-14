import re

def passChecker():
    '''Takes a string and compares to see if the string is atleast 8 characters
       long, has atleast 1 uppercase letter , 1 digit and a special character.
    '''
    while True:
        pswd = input('A strong password is defined as one that is at least eight characters long,\n contains both uppercase and lowercase characters, and has at least one digit.\
                     \n Please enter new password: ')

        while len(pswd) < 8:
            print('Password is too short enter longer password!')
            pswd = input('Please enter new password: ')

        uppercaseCounter = 0
        digitCounter = 0
        indxCounter = 0
        spCharCounter = 0
        spCounter = 0

        for i in range(len(pswd)):
            regxL = re.compile(r'[A-Z]')
            matchL = regxL.search(pswd[indxCounter])
            regxD = re.compile(r'\d')
            matchD = regxD.search(pswd[indxCounter])
            regxS = re.compile(r'\s')
            matchS = regxS.search(pswd[indxCounter])
            regxSp = re.compile(r'[!|@|#|$|%|^|&|*]')
            matchSp = regxSp.search(pswd[indxCounter])

            if matchL:
                uppercaseCounter +=1
            elif matchD:
                digitCounter +=1
            elif matchS:
                spCounter +=1
            elif matchSp:
                spCharCounter +=1

            indxCounter +=1

        if (uppercaseCounter == 0) or (digitCounter == 0) or (spCounter > 0) or (spCharCounter == 0):
            print('Password does not meet the requirements!')
        else:
            print('Password meets the requirements!')
            quit()

passChecker()
