N = int(input())

extension = dict()
for _ in range(N):
    word = input().split('.')
    if word[1] in extension:
        extension[word[1]] += 1
    else:
        extension[word[1]] = 1

[print(key, value) for (key, value) in sorted(extension.items())]
