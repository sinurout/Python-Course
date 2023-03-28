A = [3,7,5,6,1,81,43]

for i in range (0,len(A)):
    for j in range (0,len(A)-1):
        if A[j]>A[j+1]:
            c=A[j]
            A[j]=A[j+1]
            A[j+1]=c
print(A)
