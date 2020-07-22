def normal_string(string):
    res = ""
    length = len(string)

    for i in range(length):

        if string[i].isalpha():
            res += string[i]

        elif ' ' == string[i] and i:
            if ' ' != string[i - 1]:
                res += ' '

    if ' ' == res[-1]:
        res = res[:-2]

    return res.lower()
