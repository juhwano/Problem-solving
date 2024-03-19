words = dict()
string = input().upper()

for char in string:
    if char in words:
        words[char] += 1
    else:
        words[char] = 1

alphabet = [key for key, value in words.items() if max(
    words.values()) == value]

if len(alphabet) > 1:
    print('?')
else:
    print(alphabet[0])
