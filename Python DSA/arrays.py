import array as arr

#1. appending lists to array : 
#extra codes are for binary search
li = [1,2,4]
array_ = arr.array('i', [3,5,6])
len_arr = len(array_)
print(len_arr)
lo = 0
high = len(array_) - 1
print(f'lo = {lo} and high = {high}')
array_.fromlist(li)

#2. creating an array:
#array(data_type, value list)
new_arr = arr.array('i', [1,2,3])
print("The created array is : ", end = ' ')
for i in range(0,3):
    print(i, end = ' ') #The new created array is :  1 2 3
print("\r")

#3. adding elements: #insert(index, element)
new_arr.insert(1, 4)
new_arr.append(5)
print("The created array is : ", end = ' ')
for i in (new_arr):
    print(i, end = ' ') #1, 4, 2, 3, 5
print()

#4. removing elements
import array
arr = array.array('i', [1, 2, 3, 1, 5])
print("The new created array is : ", end="")
for i in range(0, 5):
    print(arr[i], end=" ")

print("\r")
print("The popped element is : ", end="")
print(arr.pop(2))
print("The array after popping is : ", end="")
for i in range(0, 4):
    print(arr[i], end=" ")

print("\r")
arr.remove(1)
print("The array after removing is : ", end="")

for i in range(0, 3):
    print(arr[i], end=" ")

#5. indexing same as lists

#6. searching:
#which consists of the linear, binary and ternary searches too
import array
arr = array.array('i', [1, 2, 3, 1, 2, 5])
print("The new created array is : ", end="")
for i in range(0, 6):
    print(arr[i], end=" ")

print("\r")
print("The index of 1st occurrence of 2 is : ", end="")
print(arr.index(2))
print("The index of 1st occurrence of 1 is : ", end="")
print(arr.index(1))

#7. counting
import array
my_array = array.array('i', [1, 2, 3, 4, 2, 5, 2])
count = my_array.count(2)
print("Number of occurrences of 2:", count)

#8. reversing
import array
my_array = array.array('i', [1, 2, 3, 4, 5])
print("Original array:", *my_array)
my_array.reverse()
print("Reversed array:", *my_array)

#9. extending
import array as arr 
a = arr.array('i', [1, 2, 3,4,5])
print("The before array extend  : ", end =" ")
for i in range (0, 5): 
  
    print (a[i], end =" ") 
    
print()
a.extend([6,7,8,9,10])
print("\nThe array after extend :",end=" ")

for i in range(0,10):  
  
    print(a[i],end=" ") 
    
print()
