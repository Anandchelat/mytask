# 6. Write a function that will take a string s as input and return whether s contains all letters of the alphabet (a to z) or not. It should return true for sentences like "The quick brown fox jumps over the lazy dog".

def checkPangram(s):
    List = []
    for i in range(26):
        List.append(False)

    for c in s.lower():
        if not c == " ":
            List[ord(c) - ord('a')] = True

    for ch in List:
        if ch == False:
            return False
    return True


# Driver Program to test above functions
sentence = "The quick brown fox jumps over the little lazy dog"

if (checkPangram(sentence)):
    print ('"' + sentence + '"')
    print("is a pangram")
else:
    print('"' + sentence + '"')
    print("is not a pangram")


