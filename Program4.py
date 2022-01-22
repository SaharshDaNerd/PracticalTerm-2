#Find frequency of an element in a list
x = input("Enter the list: ")
list1 = x.split()
element = input("Enter the element to be searched: ")
if element in list1:
    print("Element found at index:",list1.index(element),"and its frequency is:",list1.count(element))
else:
    print("Element not found")
