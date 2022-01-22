#Search for an element in the list
x = input("Enter the list: ")
list1 = x.split()
element = input("Enter the element to be searched: ")
if element in list1:
    print("Element found at index:",list1.index(element))
else:
    print("Element not found")
