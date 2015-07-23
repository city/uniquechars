queChars(str):
    char_set = []
    for i in range(0, len(str)):
        val = ord(str[i])
        if(val in char_set):
            return False
        char_set.append(val)
    return True
a = "abcdeffg"
print(uniqueChars(a))
