word_list = input().replace(':', '').split()

word_list = [word for word in word_list if word.endswith('s')]

result = "_".join(word_list)

print(result)
