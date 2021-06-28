# put your python code here
digits = input().split()
x = input()
result = []
start_pos = 0
for _ in digits:
    try:
        index = digits.index(x, start_pos)

        if index >= 0:
            result.append(str(index))
            start_pos = index + 1
    except ValueError:
        pass

if len(result) > 0:
    print(" ".join(result))
else:
    print("not found")
