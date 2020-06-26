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