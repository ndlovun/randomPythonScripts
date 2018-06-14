#Write a function that takes two words as an argument and returns true if
#they are anagrams (contain the exact same letters) and false otherwise.
print("Welcome to anagram comparer!")

w1 = input("Enter first word: ")
w2 = input("Enter second word: ")

def isAnagram(word1, word2):

    lword1 = word1.lower()
    lword2 = word2.lower()
    score = 0
    for i in lword1:
        if i in lword2:
            score +=1

    if score == len(word1):
        return True
    else:
        return False

ans = isAnagram(w1,w2)
print(ans)
