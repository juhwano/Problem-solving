assign_list = []

for i in range(28):
    assign_list.append(int(input()))

not_assign_list = [i for i in range(1,31) if i not in assign_list]
not_assign_list.sort()

for j in not_assign_list:
    print(j)