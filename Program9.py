l1=[0,1]
for i in range (7):
  l1.append(l1[i]+l1[i+1])
tup = tuple(l1)
print(len(tup))
print(tup)