# sort a list ascending order without using sort().

lst = [3,2,5,1,-1,-3,0,4]

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i],lst[j] = lst[j],lst[i]

print(lst)

