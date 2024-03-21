file = {}
N = int(input())
for _ in range(N):
    extension = input().split('.')[1]
    file[extension] = file.get(extension, 0) + 1

for (key, value) in sorted(file.items()):
    print("{} {}".format(key, value))
