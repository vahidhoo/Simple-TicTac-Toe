# put your python code here
input_grades = input()

grades_list_len = len(input_grades.split())

count_of_a = input_grades.count('A')

print(round(count_of_a / grades_list_len, 2))
