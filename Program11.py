sentence = input("Enter a sentence: ")
d = {}
for i in sentence:
    if i.isalpha():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    elif i.isdigit():
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
print(d)
