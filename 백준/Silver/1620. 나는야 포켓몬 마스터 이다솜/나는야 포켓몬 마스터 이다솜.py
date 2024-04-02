import sys
input = sys.stdin.readline
N, M = map(int, input().split())

pokemon_numbers = {}
pokemon_names = {}
for index in range(1, N+1):
    pokemon = input().strip()
    pokemon_numbers[index] = pokemon
    pokemon_names[pokemon] = index

for _ in range(M):
    question = input().strip()
    if question.isdigit():
        if int(question) in pokemon_numbers:
            print(pokemon_numbers[int(question)])
        else:
            print("No such pokemon number.")
    else:
        if question in pokemon_names:
            print(pokemon_names[question])
        else:
            print("No such pokemon name.")
