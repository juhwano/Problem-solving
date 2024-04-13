numbers = [int(input()) for _ in range(9)]

max_number = max(numbers)
max_number_order = numbers.index(max_number) + 1

print(max_number)
print(max_number_order)