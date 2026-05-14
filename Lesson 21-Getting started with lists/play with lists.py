L=[4 , 5 ,6 , 1 , 7 , 4 , 5 , 9 , 5 , 4 , 7]
print("Original list:" , L)

count=0
for i in L:
    count+=1

avg=count/len(L)

print("sum = ", count)
print("average = " , avg)

L.sort()
print("Smallest element is:" ,  L[0])
print("Largest element is:" , L[-1])
