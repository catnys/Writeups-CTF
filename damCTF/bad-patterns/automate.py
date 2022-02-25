def decode_bad_pattern(s):
    string_size = len(s)
    res = ""
    for i in range(0, string_size, 5):
        res += chr(ord(s[i]) - 0)
        res += chr(ord(s[i+1]) - 1)
        res += chr(ord(s[i+2]) - 2)
        res += chr(ord(s[i+3]) - 3)
        res += chr(ord(s[i+4]) - 4)
    return res


def encode_bad_pattern(s):
    string_size = len(s)
    res = ""
    for i in range(0, string_size, 5):
        res += chr(ord(s[i]) + 0)
        res += chr(ord(s[i+1]) + 1)
        res += chr(ord(s[i+2]) + 2)
        res += chr(ord(s[i+3]) + 3)
        res += chr(ord(s[i+4]) + 4)
    return res

print(encode_bad_pattern("bagelarenotwholewheatsometimes"))
