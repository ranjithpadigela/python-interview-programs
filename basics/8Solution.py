# Find a missing number greater than the last element.

A = [1, 2, 3, 4, 5, 7]

# def missing(A):
#     x = [A[i]+1 for i in range(len(A)-1) if A[i+1] != A[i]+1]

#     return x

def missing_num(numlist):
        numlist.sort()
        nums = list(range(numlist[0], numlist[-1]+1))
        return [i for i in nums if i not in numlist]



print(missing_num(A))