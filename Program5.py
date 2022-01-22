x = eval(input("Enter the list: "))
a = len(x)
if a % 2 != 0:
    a -= 1
for i in range(0,a,2):
    x[i],x[i+1] = x[i+1],x[i]
print(x)
