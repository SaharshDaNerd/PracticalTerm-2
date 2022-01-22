tup = eval(input("Enter a tuple: "))
n = tup.count(max(tup))
if n > 1:
    print("There are multiple max elements in the tuple")
elif n == 1:
    print("There is only one max element in the tuple")
else:
    print("That element is not in the tuple")
