def reverse(text:str)->str:
    word = ""
    length = len(text) - 1
    while length >=0:
        word += text[length]
        i -=1
    return word
"sa".reve