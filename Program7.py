tup = eval(input("Enter a 4 element tuple: "))
a,b,c,d = tup
print("The unpacked tuple is:",a,b,c,d)
tup = c,d,a,b
print("The new tuple is:",tup)