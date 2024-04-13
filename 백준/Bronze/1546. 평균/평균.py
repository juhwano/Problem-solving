N = int(input())
grade_list = list(map(int, input().split()))
high_grade = max(grade_list)

for i, grade in enumerate(grade_list):
    grade_list[i] = grade / high_grade * 100

print(sum(grade_list) / N)