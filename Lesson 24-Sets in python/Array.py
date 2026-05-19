import array as arr

array_num=arr.array('i' , [1 , 2 , 3 , 3 , 3 , 3 , 4 , 5])
print("Original array:"+ str(array_num))

print("Number of occurences of the number 3 in the array is " , array_num.count(3))
array_num.reverse
print("Reverse in order of the items:")
print(str(array_num))