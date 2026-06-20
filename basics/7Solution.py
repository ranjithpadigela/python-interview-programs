mylist = [2,5,6,34,52,9,7,62,1]
# it creates the new list which doesn't have empty item.
newlist = [i for i in mylist if i]
# this will create a new list which has ONLY empty items
emptylist = [i for i in mylist if not i]

print(newlist)
print(emptylist)