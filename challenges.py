def get_last_char(str):
    return str[-1]

def repeater(num, str):
    result = ''
    for i in range(num):
        result += str
    return result

print(repeater(3, 'wow such python '))
