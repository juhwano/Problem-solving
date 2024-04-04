num = input()
armor = input()
unique_list = list(map(int, input().split()))

dict = {}
count = 0

for i in unique_list:
    if int(armor) - i in dict:
        count += dict[int(armor) - i]
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

print(count)