"""Implementation no.1"""

# Time=O(N) || Space = O (N)
def CaesarCipherEncryptor(string,key):
    newLetters = []
    newKey= key % 26
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey))
    return "".join(newLetters)


def getNewLetter(letter,key):
    newLetterCode=ord(letter) + key
    return chr(newLetterCode) if newLetterCode<=122 else chr(96+newLetterCode%122)



"""Implementation no.2"""

# Time=O(N) || Space = O (N)
def CaesarCipherEncryptor(string,key):
    newLetters = []
    newKey= key % 26
    alphabets=list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getNewLetter(letter,newKey,alphabets))
    return "".join(newLetters)


def getNewLetter(letter,key,alphabets):
    newLetterCode=alphabets.index(letter)+ key
    return alphabets[newLetterCode] if newLetterCode<=25 else alphabets(-1+newLetterCode%25)
